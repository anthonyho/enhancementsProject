import math

class Case(object):

	NONCHARGES = ['3000.08', '3056pc', '3451', '3455(a)', '3454(a)', '3454(b)', \
                  'battach', 'cms', 'detain', 'enroute', 'fugitive', 'mtrda', \
                  'parole', 'probvio', 'prcs', 'rws647f', 'safekeep', 'tfwt', \
                  'notintbl']

	ENHANCEMENTS_ALL = ['186.10(c)(1)(a)', '186.10(c)(1)(b)', '186.10(c)(1)(c)', '186.10(c)(1)(d)','186.11(a)(2)', '186.11(a)(3)', \
						'186.22(b)(1)(a)', '186.22(b)(1)(b)', '186.22(b)(1)(c)', '186.26(d)', '186.33(b)(1)', '192.5', '273.4(a)', \
						'288.3(c)', '289.5(d)', '290.4(c)(1)', '290.45(e)(1)', '290.46(j)(2)', '347(a)(2)', '368(b)(2)(a)', '368(b)(2)(b)', \
						'368(b)(3)(a)', '368(b)(3)(b)', '422.75(a)', '422.75(b)', '451.1(a)(2)', '451.1(a)(3)', '451.1(a)(4)', '451.1(a)(5)', \
						'452.1(a)(2)', '452.1(a)(3)', '452.1(a)(4)', '550(g)', '593a(b)', '600(c)', '600(d)', '667.8(a)', '667.8(b)', \
						'667.85', '667.9(a)', '667.9(b)', '667.10', '667.15(a)', '667.15(b)', '667.16(a)', '667.17', '674(a)', '674(b)', \
						'675(a)', '12021.5(a)', '12021.5(b)', '12022(a)(1)', '12022(b)(1)', '12022(b)(2)', '12022(c)', '12022(d)', '12022.2(a)', \
						'12022.2(b)', '12022.3(a)', '12022.3(b)', '12022.4', '12022.5(a)', '12022.5(b)', '12022.53(b)', '12022.53(c)', \
						'12022.53(d)', '12022.53(e)', '12022.55', '12022.6(a)(1)', '12022.6(a)(2)', '12022.6(a)(3)', '12022.6(a)(4)', \
						'12022.7(a)', '12022.7(b)', '12022.7(c)', '12022.7(d)', '12022.7(e)', '12022.75(a)', '12022.75(b)', '12022.8', \
						'12022.85(a)', '12022.9', '12022.95', '12072(g)(4)', '12280(d)', '27590', '30615', '1522.01(c)', '11353.1(a)(1)', \
						'11353.1(a)(2)', '11353.1(a)(3)', '11353.4(a)', '11353.4(b)', '11353.6(b)', '11353.6(c)', '11356.5(a)(1)', '11356.5(a)(2)', \
						'11356.5(a)(3)', '11370.4(a)(1)', '11370.4(a)(2)', '11370.4(a)(3)', '11370.4(a)(4)', '11370.4(a)(5)', '11370.4(a)(6)', \
						'11370.4(b)(1)', '11370.4(b)(2)', '11370.4(b)(3)', '11370.4(b)(4)', '11379.7(a)', '11379.7(b)', '11379.8(a)(1)', \
						'11379.8(a)(2)', '11379.8(a)(3)', '11379.8(a)(4)', '11379.9(a)', '11380.1(a)(1)', '11380.1(a)(2)', '11380.1(a)(3)', \
						'11380.7(a)', '25189.5(e)', '25189.7(c)', '20001(c)', '23558', '23566(c)', '10980(h)(1)(a)', '10980(h)(1)(b)', \
						'10980(h)(1)(c)', '10980(h)(1)(d)', '14107(d)']

	def __init__(self, caseuid):
		self.uid = caseuid								# string
		self.race = None 								# string
		self.sex = None 								# string
		self.dob = None 								# Timestamp
		self.arrest = None	 							# Timestamp
		self.origchrg = None	 						# list of tuples of strings
		self.filedchrg = None	 						# list of tuples of strings
		self.casetype = None	 						# string
		self.crimetype = None	 						# string
		self.crimedescr = None		 					# string
		self.origdisp = None	 						# int
		self.recentdisp = None		 					# int
		self.origdispdate = None		 				# Timestamp
		self.recentdispdate = None			 			# Timestamp


	def updateRace(self, race):
		if race:
			self.race = race

	def updateSex(self, sex):
		if sex:
			self.sex = sex

	def updateDOB(self, dob):
		if dob:
			self.dob = dob.date()

	def updateArrestDate(self, arrest):
		if arrest:
			self.arrest = arrest.date()

	def updateOrigChrg(self, origchrg):
		if not origchrg or (type(origchrg) is float and math.isnan(origchrg)):
			return

		charges = (origchrg.lower()).split(',')
		nonch = []							# non-charges
		base = []							# base charges
		enh = []							# enhancements

		for i in range(len(charges)):
			if (charges[i] in nonch) or (charges[i] in base) or (charges[i] in enh) or not charges[i]:
				continue

			if charges[i] in self.NONCHARGES:
				nonch.append(charges[i])
			elif charges[i] in self.ENHANCEMENTS_ALL:
				enh.append(charges[i])
			else:
				base.append(charges[i])

		self.origchrg = (nonch, base, enh)

	def updateFiledChrg(self, filedchrg):
		if not filedchrg or (type(filedchrg) is float and math.isnan(filedchrg)):
			return

		charges = (filedchrg.lower()).split(',')

		nonch = []							# non-charges
		base = []							# base charges
		enh = []							# enhancements

		for i in range(len(charges)):
			if (charges[i] in nonch) or (charges[i] in base) or (charges[i] in enh) or not charges[i]:
				continue

			if charges[i] in self.NONCHARGES:
				nonch.append(charges[i])
			elif charges[i] in self.ENHANCEMENTS_ALL:
				enh.append(charges[i])
			else:
				base.append(charges[i])

		self.filedchrg = (nonch, base, enh)

	def updateCaseType(self, casetype):
		if casetype:
			self.casetype = casetype

	def updateCrimeType(self, crimetype):
		if crimetype:
			self.crimetype = crimetype

	def updateCrimeDescr(self, crimedescr):
		if crimedescr:
			self.crimedescr = crimedescr

	def updateOrigDisp(self, origdisp):
		if type(origdisp) is not unicode and (not (math.isnan(origdisp))):
			self.origdisp = int(origdisp)

	def updateRecentDisp(self, recentdisp):
		if type(recentdisp) is not unicode and (not (math.isnan(recentdisp))):
			self.recentdisp = int(recentdisp)

	def updateOrigDispDate(self, origdispdate):
		if origdispdate:
			self.origdispdate = origdispdate.date()

	def updateRecentDispDate(self, recentdispdate):
		if recentdispdate:
			self.recentdispdate = recentdispdate.date()

	def updateCaseData(self, race, sex, dob, arrest, origchrg, filedchrg, casetype, crimetype, crimedescr):
		self.updateRace(race)
		self.updateSex(sex)
		self.updateDOB(dob)
		self.updateArrestDate(arrest)
		self.updateOrigChrg(origchrg)
		self.updateFiledChrg(filedchrg)
		self.updateCaseType(casetype)
		self.updateCrimeType(crimetype)
		self.updateCrimeDescr(crimedescr)

	def updateDispData(self, origdisp, origdate, recentdisp, recentdate):
		self.updateOrigDisp(origdisp)
		self.updateOrigDispDate(origdate)
		self.updateRecentDisp(recentdisp)
		self.updateRecentDispDate(recentdate)

	def printData(self):
		print 'Case UID:', self.uid
		print 'Race:', self.race
		print 'Sex:', self.sex
		print 'DOB:', self.dob
		print 'Arrest Date:', self.arrest
		print 'Original Charges:'
		print self.origchrg
		print 'Filed Charges:'
		print self.filedchrg
		print 'Original Disposition:', self.origdisp
		print 'Recent Disposition:', self.recentdisp

	def getFiledChrg(self):
		return self.filedchrg

