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



def strip_extra_space(aStr):
	"""Takes a string with multiple
	spaces inbetween and returns a string
	with single space eg 'how   are  you  joy  ."""
	import re
	line = ' '.join(aStr.split())
	line = re.sub(r'\s+([.,!?])', r'\1',line)
	return line





