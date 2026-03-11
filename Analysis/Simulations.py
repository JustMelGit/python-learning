class Location(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def move(self, deltaX, deltaY):
		return Location(self.x + deltaX, self.y + deltaY)

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def distFrom(self, other):
		ox = other.x
		oy = other.y
		XDist = self.x - ox
		YDist = self.y - oy
		return (XDist**2 + YDist**2)**0.5

	def __str__(self):
		return "<" + str(self.x) + "," + str(self.y) + ">"



class Field(object):
	def __init__(self):
		self.drunks = {}

	def addDrunk(self, drunk, loc):
		if drunk in self.drunks:
			raise ValueError("Duplicate drunk")
		else:
			self.drunks[drunk] = loc

	def moveDrunk(self, drunk):
		if not drunk in self.drunks:
			raise ValueError("Drunk not in field")
		XDist, YDist = drunk.takeStep()
		currentLocation = self.drunks[drunk]
		self.drunks[drunk] = currentLocation.move(XDist, YDist)

	def getLoc(self, drunk):
		if not drunk in self.drunks:
			raiseValueError("Drunk not in field")
		return self.drunks[drunk]


class Drunk(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return "This drunk is named " + self.name

import random

class UsualDrunk(Drunk):
	def takeStep(self):
		stepChoices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
		return random.choice(stepChoices)



def walk(f, d, numSteps):
	start = f.getLoc(d)
	for s in range(numSteps):
		f.moveDrunk(d)
	return(start.distFrom(f.getLoc(d)))

def simwalks(numSteps, numTrials):
	homor = UsualDrunk("Homor")
	origin = Location(0,0)
	distances = []
	for t in range(numTrials):
		f = Field()
		f.addDrunk(homor, origin)
		distances.append(walk(f, homor, numSteps))
	return distances

def drunkTest(numTrials = 10):
	for numSteps in [10, 100, 1000, 10000]:
		distances = simwalks(numSteps, numTrials)
		print(" Random walk of " + str(numSteps) + " steps")
		print(" mean = " , sum(distances)/len(distances))
		print(" max = " , max(distances), "min =", min(distances))

g = drunkTest()
print(g)

