def stripExt(aStr,sep):
	"""Takes a string with multiple
	spaces inbetween and returns a string
	with single space"""
	i = 0
	line = ''
	space = False
	aStr = aStr.strip()
	while i<len(aStr):
		for e in aStr:
			i+=1
			if e !=sep:
				if not space:
					line+=e
				else:
					line = line + sep + e
					space = False
			else:
				space = True
	return line


# def stripTab(aStr):
# 	"""Takes a string with multiple
# 	spaces inbetween and returns a string
# 	with single space"""
# 	i = 0
# 	line = ''
# 	space = False
# 	aStr = aStr.strip()
# 	while i<len(aStr):
# 		for e in aStr:
# 			i+=1
# 			if e !='	':
# 				if not space:
# 					line+=e
# 				else:
# 					line = line + '	' + e
# 					space = False
# 			else:
# 				space = True
# 	return line

# print(stripExt('	Joy			how		are				you		','	'))
print(stripExt('    Joy    how  are  you',' '))
# print(stripTab('BASE FRAME		PIPE	323.9mm O.D. x	15.88mm W.T.	III Gr.S 355.KL0.Z35		2.794	8.382	120.565	1,011'))

# print('Joy  girl')

# print(stripExtSpace('BASE FRAME		PIPE	323.9mm O.D. x	15.88mm W.T.	III Gr.S 355.KL0.Z35		2.794	8.382	120.565	1,011'))

# fi = open(r'C:\Users\gnl999935\Desktop\New folder\Structure GA.txt','r')

# for e in fi:
# 	print(stripExtSpace(e))


# Joygirl
# Jane