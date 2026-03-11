class doc(object):
	def __init__(self,file):
		self.file = file

	def lines(self,pat):
		f = open(self.file,'r',encoding='utf-8')
		yield ''
		for line in f: yield line
		yield '02/09/22'
		# pat:item pattern
		f.close()

	def blocks(self,pat):
		'''takes a file object and return list
		of blocks conforming to pat'''
		import re
		block = []
		for line in self.lines(pat):
			if not (re.match(pat, line)): 
				block.append(line.strip())
			elif block and (re.match(pat,line)):
				yield block
				block = [line.strip()]


	def getBlocks(self,pat):
		bl = list(self.blocks(pat))[1:]
		return bl
	
	def blocksFile(self,itemPat,nextItemPat):
		'''takes a file object and returns
		a dic contain itemlist and items '''
		import re
		i = 0
		exams = {}
		inside = False
		for l in open(self.file,'r',encoding = 'utf8'):
			if re.match(itemPat,l):
				i+=1
				inside = True
				exams[i] = []
				exams[i].append(l)

			elif inside and exams[i] and not re.match(nextItemPat,l):
				if l!='':
					exams[i].append(l.strip())
			else:
				inside = False
		return exams



def scripExtSpace(aStr):
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
			if e !=' ':
				if not space:
					line+=e
				else:
					line = line + ' ' + e
					space = False
			else:
				space = True
	return line





fi = r'C:\Users\gnl999935\Documents\schedule1.txt'


schedule = doc(fi)

pat = r'\d+/\d+/\d+'
for e in schedule.getBlocks(pat):
	print(e)
	print()






