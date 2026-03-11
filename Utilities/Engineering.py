import math
from math import pi as pi

def sin(ang):
	import math
	return math.sin(ang*math.pi/180)

def cos(ang):
	import math
	return math.cos(ang*math.pi/180)

def tan(ang):
	import math
	return math.tan(ang*math.pi/180)

def asin(ang):
	import math
	return math.asin(ang)*180/math.pi

def acos(ang):
	import math
	return math.acos(ang)*180/math.pi

def atan(ang):
	import math
	return math.atan(ang)*180/math.pi



def resolve(angles):
	import numpy as np

	ver = np.array([angle[0]*sin(angle[1]) for angle in angles])
	hor = np.array([angle[0]*cos(angle[1]) for angle in angles])


	return (ver.sum()**2 + hor.sum()**2)**0.5, atan(ver.sum()/hor.sum())
	

# print(resolve([(20,0),(30,30),(40,60),(50,90),(60,120)]))

# print(sin(30)**2+cos(30)**2)

def cAreaRod(dia):
	import math
	area = pi/4*dia**2
	return area

def torque(p,N):
	return(p*60/(2*pi*N))

def dia(p,N,sShear):
	return((torque(p,N)*16)/(pi*sShear))**(1/3)

def Id(D,t):
	return(D-2*t)

# print(dia(20*10**3,200,42*10**6))

P = 'P'
A = 'A'
l = 'l'
E = 'E'
cd = 'cd'
cl = 'cl'
poi = 'poi'
d = 'd'
stress = 'stress'


class material():
	import math
	from math import pi as pi
	def __init__(self):
		#properties of the material
		
		self.prop = {}

	def areaP(self,d):
		try:
			self.prop['A'] = pi/4 *d**2
			return(pi/4 *d**2)
		except:
			print('not enough paramaters for area')

	def areaPH(self,D,d):
		try:
			self.prop[A] = pi/4 *(D**2-d**2)
			return(pi/4 *(D**2-d**2))
		except:
			print('not enough paramaters for area')

	def props(self,values):
		self.prop.update(values)
		# for propname,value in values:
		# 	self.prop[propname:value]

	def getprops(self):
		for k,v in self.prop.items():
			print(k,v)

	def stress(self):
		if self.prop.setdefault('stress',None):
			return(self.prop['stress'])
		else:
			try:
				self.prop['stress'] = self.prop['P']/self.prop['A']
				return(self.prop['P']/self.prop['A'])
			except:
				print('not enough paramaters for stress')


	def linstrain(self):
		try:
			self.prop['linstrain'] = self.prop['cl']/self.prop['l']
			return(self.prop['cl']/self.prop['l'])
		except:

			try:
				self.prop['linstrain'] = self.stress()/self.prop['E']
				return(self.stress()/self.prop['E'])
		
			except:


				print('not enough paramaters linstrain')

	def latstrain(self):
		if self.prop.setdefault('latstrain',None):
			return(self.prop['latstrain'])
		else:
			try:
				self.prop['latstrain'] = self.prop['cd']/self.prop['d']
				return(self.prop['cd']/self.prop['d'])
			except:
				try:
					self.prop['latstrain'] = self.prop['linstrain']*self.prop['poi']
					return(self.prop['linstrain']*self.prop['poi'])
				except:
					print('not enough paramaters for latstrain')

	def poisson(self):
		if self.prop.setdefault('poi',None):

			return(self.prop['poi'])
		else:
			try:
				self.prop['poi'] = self.prop['latstrain']/self.prop['linstrain']
				return(self.prop['latstrain']/self.prop['linstrain'])
			except:
				try:
					self.prop['poi'] = self.prop['E']/(2*self.prop['C'])-1
					self.prop['m'] = 1/(self.prop['E']/(2*self.prop['C'])-1)
					return(self.prop['E']/(2*self.prop['C'])-1)
				except:
					print('not enough paramaters poisson')


	def extension(self):
		if self.prop.setdefault('cl',None):
			return(self.prop['cl'])
		else:
			try:
				# print(self.linstrain()*self.prop['l'],'m')
				# print(self.linstrain()*self.prop['l']*1000,'mm')
				self.prop['cl'] = self.linstrain()*self.prop['l']
				return(self.linstrain()*self.prop['l'])

			except:
				print('not enough paramaters for extension')

	def modulus(self):
		if self.prop.setdefault('E',None):
			return(self.prop['E'])
		else:
			try:
				self.prop['E'] = self.stress()/self.linstrain()
				return(self.stress())
			except:
				print('not enough paramaters for modulus')

	
	def bulk(self):
		try:
			return(self.prop['m']*self.prop['E']/(3*self.prop['m']-6))
		except:
			print('not enough paramaters for bulk')


# cyl = material()
# cyl.props({E:110*10**9,'C':42*10**9,d:0.0375,l:2.4,cl:0.0025})
# cyl.poisson()
# cyl.bulk()
# cyl.linstrain()
# cyl.latstrain()



# cyl.getprops()
# steelRod = material()
# steelRod.props({A:0.02**2,l:0.05,P:100*10**3,E:2.14*10**11})
cyll = material()
cyll.props({E:100*10**9,P:50*10**3,l:0.6,A:1000*10**(-6)})
# cyll.areaP(0.05)
cyll.stress()
cyll.extension()

cyll.getprops()

# print(steelRod.extension())

# print(steelRod.strain())
# print(steelRod.stress())

# cylinder = material()
# cylinder.props({l:300,P:240,d:150,cd:0.127,cl:0.28})
# cylinder.areaP(150)
# # cylinder.stress()
# cylinder.linstrain()
# cylinder.latstrain()
# cylinder.extension()
# cylinder.modulus()
# cylinder.poisson()
# cylinder.getprops()

# stre = stress(100,0.2)
# strain(100,0.2,2.14)
# print(strain())
# print(extension(100*10**3,0.02**2,2.14*10**11,0.05))

# print(diaShaftTorque(20*10**3,200,42*10**6))
# print(torque(20*10**3,200))
# print(f'{areaRod(0.0326):.3f}')


# d = ((100*1000*4/(2*math.pi*60*10**6)))**0.5

# print(d)



