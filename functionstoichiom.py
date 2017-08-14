import re, logging, pyperclip
logging.basicConfig(filename = 'debugstoi.txt', level=logging.DEBUG, 
	format=' %(asctime)s - %(levelname)s- %(message)s')

compoundfindRegex = re.compile(r'''
	(([A-Za-z]{1,2})(\d\d?\d?))
	(([A-Za-z]{1,2})(\d\d?\d?))?
	(([A-Za-z]{1,2})(\d\d?\d?))?
	(([A-Za-z]{1,2})(\d\d?\d?))?
	(([A-Za-z]{1,2})(\d\d?\d?))?''', re.VERBOSE)

equationfindRegex = re.compile(r'''(#1(Mg1(O1H1)2)
	((\d) 
	\(
	
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(bna;as;dlba;easdfab)?
	
	\))
	
	\s?
	\+? 
	\s? 
	
	((\d) 
	\(
	
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(bna;as;dlba;easdfab)?
	
	\))?
	
	\s?
	\+? 
	\s? 
	
	((\d) 
	\(
	
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(bna;as;dlba;easdfab)?
	
	\))?
	
	\s? 
	(=)
	\s?
	
	((\d) 
	\(
	
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(bna;as;dlba;easdfab)?
	
	\))
	
	\s?
	\+? 
	\s? 
	
	((\d) 
	\(
	
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(bna;as;dlba;easdfab)?
	
	\))?
	
	\s?
	\+? 
	\s? 
	
	((\d) 
	\(
	
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(\(?([A-Za-z]{1,2})(\d\d?\d?)([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?([A-Za-z]{1,2})?(\d\d?\d?)?\)?(\d\d?\d?)?)?
	(bna;as;dlba;easdfab)?
	
	\))?
	
	
	
	
	
	
	 
	
	)''', re.VERBOSE)
alphanumericRegex = re.compile(r'[A-Za-z]') 
alphanumericRegex1 = re.compile(r'\d')
elements={'H':[1,1.008],'He':[2,4.0026],'Li':[3,16.94],'Be':[4,9.0122],'B':[5,10.81],# Equation would be like 2(H2O2) = 2(H2O) + (O2)
	'C':[6,12.011],'N':[7,14.007],'O':[8,15.999],'F':[9,18.998],'Ne':[10,20.18],
	'Na':[11,22.99],'Mg':[12,24.305],'Al':[13,26.982],'Si':[14,28.085],
	'P':[15,30.974],'S':[16,32.06],'Cl':[17,35.45],'Ar':[18,39.948],
	'K':[19,39.098],'Ca':[20,40.078],'Sc':[21,44.956],'Ti':[22,47.867],
	'V':[23,50.942],'Cr':[24,51.996],'Mn':[25,54.938],'Fe':[26,55.845],
	'Co':[27,58.933],'Ni':[28,58.693],'Cu':[29,63.546],'Zn':[30,65.38],
	'Ga':[31,69.723],'Ge':[32,72.63],'As':[33,74.922],'Se':[34,78.971],
	'Br':[35,79.904],'Kr':[36,83.798],'Rb':[37,85.468],'Sr':[38,87.62],
	'Y':[39,88.906],'Zr':[40,91.224],'Nb':[41,92.906],'Mo':[42,95.95],
	'Tc':[43,98],'Ru':[44,101.07],'Rh':[45,102.91],'Pd':[46,106.42],
	'Ag':[47,107.87],'Cd':[48,112.41],'In':[49,114.82],'Sn':[50,118.71],
	'Sb':[51,121.76],'Te':[52,127.6],'I':[53,126.9],'Xe':[54,131.29],
	'Cs':[55,132.91],'Ba':[56,137.33],'La':[57,138.91],'Ce':[58,140.12],
	'Pr':[59,140.91],'Nd':[60,144.24],'Pm':[61,145],'Sm':[62,150.36],
	'Eu':[63,151.96],'Gd':[64,157.25],'Tb':[65,158.93],'Dy':[66,162.5],
	'Ho':[67,164.93],'Er':[68,167.26],'Tm':[69,168.93],'Yb':[70,173.05],
	'Lu':[71,174.97],'Hf':[72,178.49],'Ta':[73,180.95],'W':[74,183.84],
	'Re':[75,186.21],'Os':[76,190.23],'Ir':[77,192.22],'Pt':[78,195.08],
	'Au':[79,196.97],'Hg':[80,200.59],'TI':[81,204.38],'Pb':[82,207.2],
	'Bi':[83,208.98],'Po':[84,209],'At':[85,210],'Rn':[86,222],'Fr':[87,223],
	'Ra':[88,226],'Ac':[89,227],'Th':[90,232.04],'Pa':[91,231.04],
	'U':[92,238.03],'Np':[93,237],'Pu':[94,244],'Am':[95,243],'Cm':[96,247],
	'Bk':[97,247],'Cf':[98,251],'Es':[99,252],'Fm':[100,257],'Md':[101,258],
	'No':[102,259],'Lr':[103,266],}
	
def find_eq_contents(formula): 
	logging.debug('Start of the find_eq_content function.') 
	mo = equationfindRegex.search(formula)
	listequation = list(mo.groups())
	del listequation[0]
	reactants = []
	products = []
	switch = reactants
	
	
	logging.debug('In listequation: ' + str(listequation))
	pyperclip.copy(str(listequation))
	
	#['2(Cl2K4)', '2', 'Cl2', 'Cl', '2', 'K4', 'K', '4', None, None, None, None, None, None, '3(O2)', '3', 'O2', 'O', '2', None, None, None, None, None, None, None, None, None, '5(K3)', '5', 'K3', 'K', '3', None, None, None, None, None, None, None, None, None, '=', '2(S1O4)', '2', 'S1', 'S', '1', 'O4', 'O', '4', None, None, None, None, None, None, '1(K1Cl1)', '1', 'K1', 'K', '1', 'Cl1', 'Cl', '1', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
	
	while listequation:
		for i in listequation: 
			if i == '=': 
				listequation.remove(i)
				switch = products
				break
				
				
			elif i == None:
				

				for n in listequation[:(listequation.index(i))]: 
					
					logging.debug('appending ' + n + 'to switch list.')
					switch.append(n)
				del listequation[:(listequation.index(i))]
				break
				
		for i in range(10000000): 
			try:
				if listequation[i] == None: 
					del listequation[i]
				else: 
					break
			except IndexError:   
				break

		
	logging.debug('Reactants list is ' + str(reactants)) 
	logging.debug('Products list is ' + str(products))
	

	
				

			
			
	return reactants, products

def format_eq_contents(listobject): 
	logging.info('Start of format_eq_contents')
	list1 = listobject[0]
	list2 = listobject[1]
	list1.append('as;dljkas;ldjl;kadfnjdfb;lnad;lk')
	list2.append('as;dlfjadsl;bl sas;gna;lkajllawha')
	iteration = 0
	iteration2 = 0
	dictionary = {}
	
	while list1:						# This would keep looping until list1 is empty
		for i in range(100000000):      # Check every single element in the list
			try: 
				if len(list1) == 1: 	# Deletes last value in list to break
					del list1[0]
					break
					
				elif list1[i] not in list1[0]: # Condition where value is in the value if not takes slice of list from there
					iteration += 1 
					 
					poplist = list1[:i]			# Creates sliced list containing all
					logging.info('Pop list is now ' + str(poplist))
					for n in range(10000000000): #Deleting specific contents in sliced list
						try:
							logging.info('working with ' + poplist[n]) 
							if '(' in poplist[n]: #Strips the amount of moles and parentheses in the thing
								what= list(poplist[n])
								if n== 0:
									del what[:2]
									del what[-1] 
								logging.info('Modified')
								
								
								poplist[n] = ''.join(what)
								
							
							elif alphanumericRegex.search(poplist[n]) and alphanumericRegex1.search(poplist[n]) : 
								logging.info('deleting ' + poplist[n]) # Searching only for single values and deleting ones with numbers and letters
								del poplist[n]
							else: 
								logging.info('Not deleting ' + poplist[n])
						except IndexError: 
							break	
					del list1[:i] #deletes dictionary
							
					logging.info('pop list is now' + str(poplist))
					
					
					dictionary['R' + str(iteration)] = poplist
					
					break
			except IndexError: 
				break	
	while list2:						# Like list 1 loop but in one dicitonary
		for i in range(100000000):      # Check every single element in the list
			try: 
				if len(list2) == 1: 	# Deletes last value in list to break
					del list2[0]
					break
					
				elif list2[i] not in list2[0]: # Condition where value is in the value if not takes slice of list from there
					iteration2 += 1 
					 
					poplist = list2[:i]			# Creates sliced list containing all
					logging.info('Pop list is now ' + str(poplist))
					for n in range(10000000000): #Deleting specific contents in sliced list
						try:
							logging.info('working with ' + poplist[n]) 
							if '(' in poplist[n]: #Strips the amount of moles and parentheses in the thing
								what= list(poplist[n])
								if n == 0:
									del what[:2]
									del what[-1] 
								logging.info('Modified')
								
								poplist[n] = ''.join(what)
								
							
							elif alphanumericRegex.search(poplist[n]) and alphanumericRegex1.search(poplist[n]) : 
								logging.info('deleting ' + poplist[n]) # Searching only for single values and deleting ones with numbers and letters
								del poplist[n]
							else: 
								logging.info('Not deleting ' + poplist[n])
						except IndexError: 
							break
					del list2[:i] #deletes dictionary
							
					logging.info('pop list is now' + str(poplist))
					
					logging.info('iteration: ' + str(iteration))
					
					dictionary['P' + str(iteration2)] = poplist
					
					break
			except IndexError: 
				break
	logging.info(str(dictionary))
	pyperclip.copy(str(dictionary))
	return dictionary
	
def find_mass_subcompound(compound1): 
	logging.debug('Start of find_mass_compound')
	what = list(compound1)
	logging.debug(what)
	del what[0] 
	del what[-1]
	logging.debug(what)
	newcompound = list()
	newvalue = list() 
	logging.debug(newcompound)
	mass = 0 
	for i in range(0,1000000,2):
		try: 
			if what[i] != None: 
				
				
				newcompound.append(what[i])
			else: 
				break
		except IndexError: 
			break
	logging.debug('new compound: ' + str(newcompound))
	for i in range(1,1000000,2): 
		try:
			if what[i] != None:
				newvalue.append(what[i])
			else: 
				break
		except IndexError:
			break
	logging.debug('newvalue: ' + str(newvalue))
	for i in range(100000000):
		try:
					
			mass += float(elements[newcompound[i]][1]) * float(newvalue[i])
		except IndexError: 
			break 
	return mass
			
	
	
		
def find_mass_compound(compoundformula): 
	compoundwhat = compoundformula
	compound = list()
	value = list()
	logging.debug(compoundwhat) #['Mg1(O1H1)2', '1', 'Mg', '1', '(O1H1)2', 'O', '1', 'H', '1', '2']
	for i in range(2,1000000,2):
		try: 
			if compoundwhat[i] != None: 
				if '(' and ')' in compoundwhat[i]:
					
					wh = len(compoundwhat[i]) - 2
					del compoundwhat[(i+1):(i+wh)]
					newi = compoundwhat[i][:-1]
					compound.append(newi)
				else:
					
					compound.append(compoundwhat[i])
			else: 
				break
		except IndexError: 
			break
	for i in range(3,1000000,2): 
		try:
			if compoundwhat[i] != None:
				value.append(compoundformula[i])
			else: 
				break
		except:
			break
	
			

	logging.info(compound) 
	logging.info(value)	
	mass = 0
	for i in range(100000000):
		try: 
			if compound[i] not in elements.keys():
				what = find_mass_subcompound(compound[i])
				
				mass += float(what) * float(value[i])
			else:
				
				
				
				
				mass += float(elements[compound[i]][1]) * float(value[i])
		except IndexError: 
			break 
	return mass

	
def gram_mol(formula, grams): 
	mole = int(grams)/find_mass(formula)
	return mole 
def mol_gram(formula, mol): 
	grams=find_mass_compound(formula)*mol
	return grams
def mol_ratio(topmole,bottommole): 
	return int(topmole)/int(bottommole)
def find_unit_required(equation1, given, want): 
	newformat = format_eq_contents(find_eq_contents(equation1))
	givenvalue = given[0]
	givenunit = given[1] 			# Assigning values toPuy
	givencompound = given[2] 
	wantunit = want[0] 
	wantcompound = want[1]

	for i in newformat.values(): 
		if i[0] == wantcompound: 
			wantcontents = i
			break
	for i in newformat.values(): 
		if i[0] == givencompound: 
			givencontents = i
			break
			
			
	if wantunit == 'mol': 
		if givenunit == 'mol': 
			answer = givenvalue * mol_ratio(wantcontents[1],givencontents[1])
			return answer
		elif givenunit == 'g': 
			answer = givenvalue/find_mass_compound(givencontents) * mol_ratio(wantcontents[1],givencontents[1])
			return answer
	elif wantunit== 'g': 
		if givenunit == 'mol': 
			answer = givenvalue * mol_ratio(wantcontents[1],givencontents[1])
			
			answer *= find_mass_compound(wantcontents)
		

			return answer
			
			
		elif givenunit == 'g':
			mole1 = givenvalue/find_mass_compound(givencontents)
			answer = mole1 * mol_ratio(wantcontents[1],givencontents[1])
			
			answer *= find_mass_compound(wantcontents)
		

			return answer
def find_limit_r(equation, listreactants, unit = 'g', what = 'P1'): 
	dictionary = format_eq_contents(find_eq_contents(equation))
	equation1 = equation 
	listreactants1 = listreactants 
	iteration = {}
	newvalues = list()
	for i in listreactants1: 
		
		answer = find_unit_required(equation1, i, [unit, dictionary[what][0]])
		iteration[i[2]] = answer
	for i in iteration.values(): 
		newvalues.append(i)
	newvalues.sort()
	for keys, values in iteration.items(): 
		if values == newvalues[0]: 
			v = keys + ' is the limiting reactant' 
			return v
			break
			
		
	
	
	
			
 
			
			
	
		
	

		
	
	
	
	
pyperclip.copy(find_limit_r('4(N1H3) + 5(O2) = 4(N1O1) + 6(H2O1)',[[10,'mol','O2'],[10,'mol','N1H3']]))
