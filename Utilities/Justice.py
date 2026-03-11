
class Justice(object):
	def __init__(self):
		self.courses = []
		self.keys = []
		# self.days = {'monday':[],'tueday':[], 'wednesday':[],'thurdsay':[],\
		# 					'friday':[],'saturday':[],'sunday':[]}

	def lines(self, directory):
		file = open(directory)
		for line in file: yield line
		yield '\n'
		file.close()

	def blocks(self, file):
		block = []
		for line in self.lines(file):
			if line.strip():
				block.append(line)
			elif block:
				yield block
				block = []

	def addCourse(self,name,file):
		name = {}
		for items in self.blocks(file):
			name[items[0]] = []
			name[items[0]].append(items[1:])
		self.courses.append(name)

	def dayActivities(self):
		import random
		
		keys = []
		for e in self.courses:
			for d in e:
				keys.append(d)
			picked = random.choice(keys)
			self.keys.append(picked)
			keys = []
		return self.keys


justice = Justice()



eng = r'C:\Users\Justice\Documents\Engineering.txt'
song = r'C:\Users\Justice\Documents\Kingdom Songs.txt'
pipe = r'C:\Users\Justice\Documents\Piping.txt'
file = {'Eng':eng,'Song':song,'Pipe':pipe}

justice.addCourse('Song',song)
justice.addCourse('Piping', pipe)
justice.addCourse('Engineering',eng)

# print(justice.courses)

def weekActivities(files):
	days = {'monday':[],'tueday':[], 'wednesday':[],'thurdsay':[],\
						'friday':[],'saturday':[]}
	for k in days:
		c = Justice()

		for file in files:
			c.addCourse(file[0],file[1])
		days[k] = [e.strip() for e in c.dayActivities()]
	return days






textfile = open('textfile.txt', 'a+', encoding = 'utf-8')
# 			textfile.write(text)



study = [('Eng',eng),('Song',song),('Pipe',pipe)]
IstWeek = weekActivities(study)



txt = ''
text = open(r'C:\Users\Justice\OneDrive\Documents\sche.txt','a+')
text.write('Week schedule'+'\n'*2)
for k in IstWeek:
	for e in IstWeek[k]:
		txt+=e
		if not IstWeek[k][-1]==e:
			txt+=','
	text.write(k+'\n')
	text.write(txt+'\n'*2)
	txt = ''	



