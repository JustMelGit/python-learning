# class Justice(object):
# 	self.songs = []
# 	self.engineering = []
# 	self.Monday = 
# if len(self.days[d])<21

# def Songs(file):
# 	songs = []
# 	for e in file:
# 		songs.append(e)
# 		yield songs
file = open(r'C:\Users\Justice\Desktop\Pra.txt')
class songs(object):
	def __init__(self, file):
		self.file = file
		self.days = {'monday':[],'tueday':[], 'wednesday':[],'thurdsay':[],\
					'friday':[],'saturday':[],'sunday':[]}
	def assignSongs(self):
		# days = {'monday':[],'tueday':[]}#'wednesday':[],'thurdsay':[],'friday':[],\
			#'saturday':[],'sunday':[]}
		for d in self.days:
			for e in self.file:
				self.days[d].append(e.strip())
				if len(self.days[d])==21:
					break
				# return True
	def getDays(self):
		return self.days

c = songs(file)
c.assignSongs()
print(c.getDays())





# r = assignSongs(file)
# print(r)

# for e in range(len(songs)):
# 	for d in days:
# 		days[d].append(songs[e].strip())
# 		if e>0 and e%21==0:
# 			break
# print(days)
# for d in days:
# 	for songs in d:
# 		print(d,songs)