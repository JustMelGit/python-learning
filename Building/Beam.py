import numpy as np

class beams():
	def conBeam(self,spans_loads):
		spans = len(spans_loads)
		span_prop = {}
		for n in range(len(spans_loads)):
			span_prop[n+1] = spans_loads[n]
		coff = {}
		load = {}
		for span in range(spans-1):
			coff[span+1] =[]
			coff[span+1].append(span_prop[span+1][0])
			coff[span+1].append((span_prop[span+1][0]+span_prop[span+2][0])*2)
			coff[span+1].append(span_prop[span+2][0])
			load[span+1] = (span_prop[span+1][1]*span_prop[span+1][0]**3)/4 + (span_prop[span+2][1]*span_prop[span+2][0]**3)/4
		

		left_par = [k[1] for k in coff.items()]
		total_Zeros = spans - 2
		newleft_par = []
		for i in range(len(left_par)):
			leftzeros = [0]*i
			rightzeros = [0]*(total_Zeros-len(leftzeros))
			newleft_par.append(leftzeros+left_par[i]+rightzeros)
		for li in newleft_par:
			li.pop(0)
			li.pop(-1)
		

		right_par = [k[1] for k in load.items()]

		
		eqnleft = np.array([i for i in newleft_par])
		print(eqnleft)
		eqnright = np.array([j for j in right_par])
		x = np.linalg.solve(eqnleft,eqnright)
		

		smoments = {}
		smoments['M1']=0
		for n in range(len(x)):

			smoments['M'+str(n+2)] = x[n]
		smoments['M'+str(n+3)] = 0
		
		frMoments = {}
		for f in range(len(spans_loads)):
			frMoments['Sp'+str(f+1)+'-'+str(f+2)] = 0.125*spans_loads[f][1]*spans_loads[f][0]**2

		spanMoments = {}
		for e in range(len(smoments)-1):
			spanMoments['Sp'+str(e+1)+'-'+str(e+2)] = frMoments['Sp'+str(e+1)+'-'+str(e+2)]-(smoments['M'+str(e+1)] + smoments['M'+str(e+2)])/2

		
		sForce = {}
		for e in range(len(span_prop)):
			sForce['Sh'+str(e+1)+'-'+str(e+2)] = 0.5*spans_loads[e][0]*spans_loads[e][1]+\
			(smoments['M'+str(e+1)]-smoments['M'+str(e+2)])/spans_loads[e][0]
			sForce['Sh'+str(e+2)+'-'+str(e+1)] = 0.5*spans_loads[e][0]*spans_loads[e][1]+\
			(smoments['M'+str(e+2)]-smoments['M'+str(e+1)])/spans_loads[e][0]

		return smoments,spanMoments,sForce



def resultTableM(loadings):
	results = {}
	for e in range(len(loadings)):
		b = beams()
		c = b.conBeam(loadings[e])
		results[e] = {}
		results[e]['support'] = c[0]
		results[e]['span'] = c[1]
		results[e]['shear'] = c[2]



	supports = [k for k in results[0]['support']]
	span = [k for k in results[0]['span']]
	shear = [k for k in results[0]['shear']]

	moments = supports+span

	table = {}
	for e in moments:
		table[e] = []
		for k,v in results.items():
			for ik, iv in v.items():
				if e in iv:
					table[e].append(iv[e])
					if len(table[e])==2:
						table[e].append(max(table[e]))



	print(f"BM\t\tSection\t\tLoad 1\t\tLoad 2\t\tDesign Moment")
	for k,v in table.items():
		if 'M' in k:
			print(f"support\t\t{k[1:]}\t\t{v[0]:.02f}\t\t{v[1]:.02f}\t\t{v[2]:.02f}")
		else:
			print(f"span\t\t{k[2:]}\t\t{v[0]:.02f}\t\t{v[1]:.02f}\t\t{v[2]:.02f}")



def resultTableS(loadings):
	results = {}
	for e in range(len(loadings)):
		b = beams()
		c = b.conBeam(loadings[e])
		results[e] = {}
		results[e]['shear'] = c[2]
	span = len(c[2])//2
	shear = [k for k in results[0]['shear']]

	table = {}
	for e in shear:
		table[e] = []
		for k,v in results.items():
			for ik, iv in v.items():
				if e in iv:
					table[e].append(iv[e])



	# print(f"Span\t\tSection\t\tLoad 1\t\tLoad 2\t\tDesign Moment")
	import re
	shearf = {}
	for ke in range(1,span+1):
		pat1 = '%s'%('Sh'+str(ke)+'-'+str(ke+1))
		# print(pat1)
		pat2 = '%s'%('Sh'+str(ke+1)+'-'+str(ke))
		# print(pat2)
		keyv = str(ke)+'-'+str(ke+1)
		shearf[keyv] = {}
		for  key in table:
			if re.match(pat1,key):
				shearf[keyv]['Left']=table[key]
			if re.match(pat2,key):
				shearf[keyv]['Right']=table[key]
	


	print(f"Span\t\tLoad 1\t\t\t\t\tLoad 2\t\t")
	print(f"\t\tLeft\t\tRight\t\tLeft\t\tRight")
	for keys,value in shearf.items():
		print(f"{keys}\t\t{value['Left'][0]:.01f}\t\t{value['Right'][0]:.01f}\t\t{value['Left'][1]:.01f}\t\t{value['Right'][1]:.01f}")


loading1 = [[4.2,57],[4.5,57],[4.5,57],[4.2,57]]
loading2 = [[4.2,57],[4.5,14.6],[4.5,57],[4.2,14.6]]

loadings = [loading1,loading2]

# print('\t'*4,'Moment summary')
resultTableM(loadings)
# print()
# print('\t'*4,'Shear summary')
resultTableS(loadings)

class bdesign():
	def __init__(self,fcu,fy,D,b=230,cc=25,strp=10,stl = 10):
		self.D = D
		self.cc = cc
		self.strp = strp
		self.M = None
		self.k = None
		self.z = None
		self.la = None
		self.Ast = None
		self.stl =stl
		self.fcu = fcu
		self.fy = fy
		self.b = b
		self.d = self.D -self.cc-self.strp-self.stl


	def addM(self, M):
		self.M = M
		self.k = self.M*10**6/(self.fcu*self.b*self.d**2) 
		self.z = self.d*(0.5+(0.25-self.k/0.9)**0.5)
		self.la = self.d*(0.5+(0.25-self.k/0.9)**0.5)/self.d
		self.Ast = self.M*10**6/(0.95*self.fy*self.z)


	def beamprop(self):
		return self.M,self.Ast,self.k,self.la,self.z



# bm = bdesign(25,410,450,b=230)

def beamParameters(beams, loading, moments):

	for moment in moments:
		beams(loading)



# bm.addM(112.525)
# print(bm.beamprop())

class sdesign():
	def __init__(self,fcu,fy,D,b=1000,cc=20,stl = 6):
		self.D = D
		self.cc = cc
		self.M = None
		self.k = None
		self.z = None
		self.la = None
		self.Ast = None
		self.stl =stl
		self.fcu = fcu
		self.fy = fy
		self.b = b
		self.latre = None
		self.d = self.D -self.cc-self.stl


	def addM(self, M):
		self.M = M
		self.k = self.M*10**6/(self.fcu*self.b*self.d**2) 
		self.z = self.d*(0.5+(0.25-self.k/0.9)**0.5)
		self.la = self.d*(0.5+(0.25-self.k/0.9)**0.5)/self.d
		self.Ast = self.M*10**6/(0.95*self.fy*self.z)
		self.latre = 0.13/100*self.b*self.D 


	def latre(self):
		return 0.13/100*self.b*self.D

	def prop(self):
		return self.M,self.Ast,self.latre,self.k,self.la,self.z

# sl = sdesign(25,410,150)
# sl.addM(13.612)
# print(sl.prop())

