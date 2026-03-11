class Arrange(object):
	def lines(self,file):
		f = open(file,'r',encoding='utf-8')
		for line in f: yield line
		yield 'END'
		f.close()

	def blocks(self,file):
		import re
		patb = r'[\d]+\.[\d]+ .+'
		block = []
		for line in self.lines(file):
			if not (re.match(patb, line)): 

				block.append(line.strip())

			elif block and (re.match(patb,line)):

				yield block
				
				block = [line.strip()]

	def section(self,file,pat):
		import re
		ex = 0
		exams = {}
		inside = False
		for l in self.lines(file):
			if re.match(pat,l):
				inside = True
				ke = l
				exams[ke]=[] 
				exams[ke].append(l.strip())
					

			elif inside and exams[ke] and not re.match(pat,l):
				if l!='':
					exams[ke].append(l.strip())
			
			elif re.match(pat,l):

				exams[l] = []

			else:
				inside = False
		return exams

	def arrangedoc(self,file,item,nextItem,pat):
		
		import re
		i = 0
		exams = {}
		for block in self.blocks(file):
			line = ''
			inside = False
			i+=1
			ex = 0
			exams[i] = {}
			for l in block:

				if l.startswith(item):
					inside = True
					if ex ==0:
						exams[i][ex]=line,[] 
						exams[i][ex][1].append(l.strip())
					else:
						exams[i][ex][1].append(l.strip())
						

				elif inside and exams[i][ex][1] and nextItem not in  l:
					if l!='':
						exams[i][ex][1].append(l.strip())
				
				elif re.match(pat,l):
					m = re.match(pat,l)

					line+=m.group(1)
					ex+=1
					exams[i][ex] = line,[]
					line = ''

				else:
					inside = False
		return exams


def unpackDicDic(fi,items,pats):
	examples = []
	for i in range(len(items)):

		c = Arrange()
		dic = c.arrangedoc(fi,items[i][0],items[i][1],pats[i])

		examples.append(dic)
	return examples



# fi = r'C:\Users\Justice\Ebooks\Piping\vidic.txt'
# items = [('Example','Solution'),('Solution','Example')]
# pats = [r'(Solution\.).+',r'(Example\.* [\d]+\.[\d]*).+']

# examss = unpackDicDic(fi,items,pats)

fi = r'C:\Users\Justice\Ebooks\Piping\vidic8.txt'
items = [('Example','Solution'),('Solution','Example')]
# pats = [r'(Solution\.).+',r'(Example\.* [\d]+\.[\d]*).+']

# examss = unpackDicDic(fi,items,pats)
import re
c = Arrange()
pat = r'[A-Za-z]+ [=]+? [A-z]+'

# patb = r'14\.[\d]{1,2} .+'
# patMd = r'14\.[\d]+\.?[\d]?\.?.+'
# patSS = r'%s\.[\d]+ .+'%i

def oneSection(file, chapter):
	# pattern = r'%s\.[\d]+ .+'%i
	# pattern = r'%s\.[\d]+\.?[\d]?\.?.+'%chapter
	pattern = r'chapter:%s: .+'
	c = Arrange()
	sections = c.section(file,pattern)

# print(sections)
# 	for k,v in sections.items():
# 		print()
# 		print()
# 		print()
# 		print()
# 		print(k)
# 		for e in v:
# 			# print(e)
# 			if '=' in e:
# 				print(e)


print(oneSection(fi,9))



# def sections(file, chapters):
# 	for i in range(1,chapters+1):
# 		# pattern = r'%s\.[\d]+ .+'%i
# 		pattern = r'%s\.[\d]+\.?[\d]?\.?.+'%i
# 		c = Arrange()
# 		sections = c.section(file,pattern)
	
# 	# print(sections)
# 		for k,v in sections.items():
# 			print(k)
# 			for e in v:
# 				# print(e)
# 				if '=' in e:
# 					print(e)

# oneSections(fi,8)
# def unpackDicDic1(dic):
# 	items = 0
# 	examples = {}
# 	for e in dic:
# 		items+=1
# 		examples[items] = []
# 		for key,value in e.items():
# 			if value:
# 				for insKeys, insValues in value.items():
# 					block = []
# 					for i in insValues[1]:
# 						block.append(i)
# 					if insValues[0] == 'Solution.':

# 						examples[items].append(' '.join(block))
# 					elif insValues[0] == '':

# 						examples[items].append(' '.join(block))
# 					else:
# 						block.insert(0,insValues[0])
# 						examples[items].append(block)
# 	return examples



# import re
# dic = {}
# n = 0
# pat = r'(Example\.* [\d]*\.[\d]*).+'
# examples = []
# solutions = []
# for k, v in unpackDicDic1(examss).items():
# 	if k ==1:
# 		for e in v:
# 			examples.append(e)
# 	elif k==2:
# 		for e in v:
# 			solutions.append(e)

# for i in range(len(examples)):
# 	try:
# 		m = re.match(pat,examples[i])
# 		dic[m.group(1).strip()] = [examples[i]]
# 	except:
# 		# print(examples[i])
# 		print()

# for k in dic:
# 	for s in solutions:
# 		if s[0].strip() == k:
# 			dic[k].append(s)

# for ke, i in dic.items():
# 	# print(ke)
# 	print(i[0])
# 	for e in i[1][1:]:
# 		print(e)
# 		# if '=' in e or len(e)>3:
# 			# print(e)
# 		# print(e)
# 	print()

# # print(dic)
