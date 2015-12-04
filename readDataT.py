import pandas as pd
import case

folder2014 = '/home/todor/Documents/Projects/Mass Incarceration/2014/'
folder2013 = '/home/todor/Documents/Projects/Mass Incarceration/2013/'
folder2012 = '/home/todor/Documents/Projects/Mass Incarceration/2012/'
folder2011 = '/home/todor/Documents/Projects/Mass Incarceration/2011/'
folder2010 = '/home/todor/Documents/Projects/Mass Incarceration/2010/'
folder2009 = '/home/todor/Documents/Projects/Mass Incarceration/2009/'
folder2008 = '/home/todor/Documents/Projects/Mass Incarceration/2008/'

file2014_1 = '150421_FiledCases_2014_CaseDispos_DeID.xlsx'
file2013_1 = '150421_FiledCases_2013_CaseDispos_DeID.xlsx'
file2012_1 = '150408_FiledCases_2012_CaseDispos_DeID.xlsx'
file2011_1 = '150407_FiledCases_2011_CaseDispos_DeID.xlsx'
file2010_1 = '150407_FiledCases_2010_CaseDispos_DeID.xlsx'
file2009_1 = '150407_FiledCases_2009_CaseDispos_DeID.xlsx'
file2008_1 = '150407_FiledCases_2008_CaseDispos_DeID.xlsx'

file2014_2 = '150421_FiledCases_2014_Charges_DeID.xlsx'
file2013_2 = '150421_FiledCases_2013_Charges_DeID.xlsx'
file2012_2 = '150408_FiledCases_2012_Charges_DeID.xlsx'
file2011_2 = '150407_FiledCases_2011_Charges_DeID.xlsx'
file2010_2 = '150407_FiledCases_2010_Charges_DeID.xlsx'
file2009_2 = '150407_FiledCases_2009_Charges_DeID.xlsx'
file2008_2 = '150407_FiledCases_2008_Charges_DeID.xlsx'

file2014_3 = '150421_FiledCases_2014_CountDispos_DeID.xlsx'
file2014_4 = '150421_FiledCases_2014_SNEvents_DeID.xlsx'

CaseDispos2014 = pd.read_excel(folder2014 + file2014_1)
CaseDispos2013 = pd.read_excel(folder2013 + file2013_1)
CaseDispos2012 = pd.read_excel(folder2012 + file2012_1)
CaseDispos2011 = pd.read_excel(folder2011 + file2011_1)
CaseDispos2010 = pd.read_excel(folder2010 + file2010_1)
CaseDispos2009 = pd.read_excel(folder2009 + file2009_1)
CaseDispos2008 = pd.read_excel(folder2008 + file2008_1)

Charges2014 = pd.read_excel(folder2014 + file2014_2)
Charges2013 = pd.read_excel(folder2013 + file2013_2)
Charges2012 = pd.read_excel(folder2012 + file2012_2)
Charges2011 = pd.read_excel(folder2011 + file2011_2)
Charges2010 = pd.read_excel(folder2010 + file2010_2)
Charges2009 = pd.read_excel(folder2009 + file2009_2)
Charges2008 = pd.read_excel(folder2008 + file2008_2)

CaseDispos = {}
CaseDispos[2008] = CaseDispos2008
CaseDispos[2009] = CaseDispos2009
CaseDispos[2010] = CaseDispos2010
CaseDispos[2011] = CaseDispos2011
CaseDispos[2012] = CaseDispos2012
CaseDispos[2013] = CaseDispos2013
CaseDispos[2014] = CaseDispos2014

Charges = {}
Charges[2014] = Charges2014
Charges[2013] = Charges2013
Charges[2012] = Charges2012
Charges[2011] = Charges2011
Charges[2010] = Charges2010
Charges[2009] = Charges2009
Charges[2008] = Charges2008

#f3 = pd.read_excel(folder2014 + f2014_3)
#f4 = pd.read_excel(folder2014 + f2014_4)

"""
noncharges = ['3000.08', '3056pc', '3451', '3455(a)', '3454(a)', '3454(b)', \
				'battach', 'cms', 'detain', 'enroute', 'fugitive', 'mtrda', \
				'parole', 'probvio', 'prcs', 'rws647f', 'safekeep', 'tfwt', \
				'notintbl']
"""

"""
#enhancements_whitecoll = ['186.10(c)(1)(a)', '186.10(c)(1)(b)', '186.10(c)(1)(c)', '186.10(c)(1)(d)','186.11(a)(2)', '186.11(a)(3)']
#enhancements_g_gang = ['186.22(b)(1)(a)', '186.22(b)(1)(b)', '186.22(b)(1)(c)', '186.26(d)', '186.33(b)(1)', '192.5']
#enhancements_1 = ['273.4(a)', '288.3(c)', '289.5(d)', '290.4(c)(1)', '290.45(e)(1)', '290.46(j)(2)', '347(a)(2)', '368(b)(2)(a)', '']
enhancements__g_prior
enhancements_g_weapons
enhancements_g_impact
enhancements_g_victim
enhancements_g_other
enhancements_s_drug
enhancements_s_sex
enhancements_s_property
enhancements_s_dui
enhancements_s_other = ['186.10(c)(1)(a)', '186.10(c)(1)(b)', '186.10(c)(1)(c)', '186.10(c)(1)(d)','186.11(a)(2)', '186.11(a)(3)']
"""

enhancements_all = ['186.10(c)(1)(a)', '186.10(c)(1)(b)', '186.10(c)(1)(c)', '186.10(c)(1)(d)','186.11(a)(2)', '186.11(a)(3)', \
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

caseList = {}

for j in range(2008, 2015):
	for i in range(len(Charges[j]['Case UID'])):
		caseuid = Charges[j]['Case UID'][i]
		if caseuid not in caseList:
			newcase = case.Case(caseuid)
			newcase.updateCaseData(Charges[j]['Race'][i], Charges[j]['Defendant Sex'][i], Charges[j]['DOB'][i], Charges[j]['Arrest Date'][i], \
									Charges[j]['List of Original Charges'][i], Charges[j]['List of Filed Charges'][i], Charges[j]['Filed Case Type'][i], \
									Charges[j]['Crime Type'][i], Charges[j]['Crime Description'][i])
			caseList[caseuid] = newcase
		#else:
		#	print 'Found:', caseuid, i, j

for j in range(2008, 2015):
	for i in range(len(CaseDispos[j]['Original Disposition'])):
		caseuid = CaseDispos[j]['Case UID'][i]
		if caseuid in caseList:
			caseList[caseuid].updateDispData(CaseDispos[j]['Original Disposition'][i], CaseDispos[j]['Original Disposition Date'][i], \
				                             CaseDispos[j]['Recent Dispo Code'][i], CaseDispos[j]['Recent Disposition Date'][i])
		#else:
		#	print 'Not found:', caseuid, i, j


commonEnh = []
commonBase = []

enhCounts = {}
for enh in enhancements_all:
	enhCounts[enh] = 0

enh1BaseCounts = {}
enh2BaseCounts = {}



base1Counts = 0
base2Counts = 0
base3Counts = 0


commonEnhCheat = []

for case in caseList:
	filedchrg = caseList[case].getFiledChrg()
	if filedchrg:
		for enh in filedchrg[2]:
			enhCounts[enh] += 1

		"""
		if '12022.7(a)' in filedchrg[2]:
			for base in filedchrg[1]:
				if base not in enh1BaseCounts:
					enh1BaseCounts[base] = 0
				enh1BaseCounts[base] += 1

		if '12022(b)(1)' in filedchrg[2]:
			for base in filedchrg[1]:
				if base not in enh2BaseCounts:
					enh2BaseCounts[base] = 0
				enh2BaseCounts[base] += 1

		if '245(a)(1)' in filedchrg[1] or '245(a)1' in filedchrg[1]:
			base1Counts += 1

		if '245(a)(4)' in filedchrg[1] or '245(a)4' in filedchrg[1]:
			base2Counts += 1

		if '243(d)' in filedchrg[1]:
			base3Counts += 1
		"""

for enh in enhCounts:
	if enhCounts[enh] > 10:
		commonEnh.append(enh)

#print commonEnh


enhBaseCounts = {}
for enh in commonEnh:
	enhBaseCounts[enh] = {}

for case in caseList:
	filedchrg = caseList[case].getFiledChrg()
	if filedchrg:
		for enh in filedchrg[2]:
			if enh in commonEnh:
				for base in filedchrg[1]:
					if base not in enhBaseCounts[enh]:
						enhBaseCounts[enh][base] = 0
					enhBaseCounts[enh][base] += 1

for enh in commonEnh:
	#print enhCounts[enh]
	for base in enhBaseCounts[enh]:
		if enhBaseCounts[enh][base] > 30:
			#print enh, base, enhBaseCounts[enh][base]
			if base not in commonBase:
				commonBase.append(base)

	#print

print commonBase, len(commonBase)

baseCounts = {}
for base in commonBase:
	baseCounts[base] = 0
for case in caseList:
	filedchrg = caseList[case].getFiledChrg()
	if filedchrg:
		for base in filedchrg[1]:
			if base in commonBase:
				baseCounts[base] += 1

#for base in baseCounts:
#	print base, baseCounts[base]

importantPairs = []
for enh in commonEnh:
	for base in enhBaseCounts[enh]:
		if (enh, base) in importantPairs:
			continue
		if (base in commonBase) and (10 * enhBaseCounts[enh][base] > baseCounts[base]):
			importantPairs.append((enh, base))


importantEnh = []
importantBase = []

for pair in importantPairs:
	if pair[0] not in importantEnh:
		importantEnh.append(pair[0])
	if pair[1] not in importantBase:
		importantBase.append(pair[1])

print importantEnh
print
print importantBase

"""
for base in enh1BaseCounts:
	if enh1BaseCounts[base] > 100:
		print base, enh1BaseCounts[base]

print

for base in enh2BaseCounts:
	if enh2BaseCounts[base] > 100:
		print base, enh2BaseCounts[base]

print

print '245(a)(1)', base1Counts
print '245(a)(4)', base2Counts
print '243(d)', base3Counts
"""