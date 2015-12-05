import case

def analyzeData(caseList):
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
	"""
	enhancements_all = ['186.10c1a', '186.10c1b', '186.10c1c', '186.10c1d','186.11a2', '186.11a3', \
						'186.22b1a', '186.22b1b', '186.22b1c', '186.26d', '186.33b1', '192.5', '273.4a', \
						'288.3c', '289.5d', '290.4c1', '290.45e1', '290.46j2', '347a2', '368b2a', '368b2b', \
						'368b3a', '368b3b', '422.75a', '422.75b', '451.1a2', '451.1a3', '451.1a4', '451.1a5', \
						'452.1a2', '452.1a3', '452.1a4', '550g', '593ab', '600c', '600d', '667.8a', '667.8b', \
						'667.85', '667.9a', '667.9b', '667.10', '667.15a', '667.15b', '667.16a', '667.17', '674a', '674b', \
						'675a', '12021.5a', '12021.5b', '12022a1', '12022b1', '12022b2', '12022c', '12022d', '12022.2a', \
						'12022.2b', '12022.3a', '12022.3b', '12022.4', '12022.5a', '12022.5b', '12022.53b', '12022.53c', \
						'12022.53d', '12022.53e', '12022.55', '12022.6a1', '12022.6a2', '12022.6a3', '12022.6a4', \
						'12022.7a', '12022.7b', '12022.7c', '12022.7d', '12022.7e', '12022.75a', '12022.75b', '12022.8', \
						'12022.85a', '12022.9', '12022.95', '12072g4', '12280d', '27590', '30615', '1522.01c', '11353.1a1', \
						'11353.1a2', '11353.1a3', '11353.4a', '11353.4b', '11353.6b', '11353.6c', '11356.5a1', '11356.5a2', \
						'11356.5a3', '11370.4a1', '11370.4a2', '11370.4a3', '11370.4a4', '11370.4a5', '11370.4a6', \
						'11370.4b1', '11370.4b2', '11370.4b3', '11370.4b4', '11379.7a', '11379.7b', '11379.8a1', \
						'11379.8a2', '11379.8a3', '11379.8a4', '11379.9a', '11380.1a1', '11380.1a2', '11380.1a3', \
						'11380.7a', '25189.5e', '25189.7c', '20001c', '23558', '23566c', '10980h1a', '10980h1b', \
						'10980h1c', '10980h1d', '14107d']


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
			if '12022.7a' in filedchrg[2]:
				for base in filedchrg[1]:
					if base not in enh1BaseCounts:
						enh1BaseCounts[base] = 0
					enh1BaseCounts[base] += 1

			if '12022b1' in filedchrg[2]:
				for base in filedchrg[1]:
					if base not in enh2BaseCounts:
						enh2BaseCounts[base] = 0
					enh2BaseCounts[base] += 1

			if '245a1' in filedchrg[1] or '245a1' in filedchrg[1]:
				base1Counts += 1

			if '245a4' in filedchrg[1] or '245a4' in filedchrg[1]:
				base2Counts += 1

			if '243d' in filedchrg[1]:
				base3Counts += 1
			"""

	for enh in enhCounts:
		if enhCounts[enh] > 20:
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
			if enhBaseCounts[enh][base] > 100:
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
			if (base in commonBase) and (5 * enhBaseCounts[enh][base] > baseCounts[base]):
				importantPairs.append((enh, base))



	importantEnh = []
	importantBase = []

	print

	for pair in importantPairs:
		print pair[0], pair[1], enhBaseCounts[pair[0]][pair[1]], baseCounts[pair[1]]
		if pair[0] not in importantEnh:
			importantEnh.append(pair[0])
		if pair[1] not in importantBase:
			importantBase.append(pair[1])

	print 
	print importantEnh
	print
	print importantBase
	print


	base_all = []
	for case in caseList:
		filedchrg = caseList[case].getFiledChrg()
		if filedchrg:
			for base in filedchrg[1]:
				if base not in base_all:
					base_all.append(base)
	"""
	print base_all, len(base_all)
	print

	for base in base_all:
		if base.find('(') != -1:
			print base
	"""
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
	