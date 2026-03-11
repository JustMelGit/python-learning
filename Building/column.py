class columnload():
	def __init__(self,fcu,fy,Lload,patAllw,fhs,bfhs,rLoad,\
		wLoad,wallH,slabdp,fBeamH,fBeamW,rBeamH,rBeamW,\
		colH,colW,roofload,condens=24):

		self.fcu = fcu
		self.fy = fy
		self.Lload = Lload
		self.patAllw = patAllw
		self.fhs = fhs
		self.bfhs = bfhs
		self.rLoad = rLoad
		self.wLoad = wLoad
		self.wallH = wallH
		self.slabdp = slabdp
		self.condens = condens
		self.fBeamH = fBeamH
		self.fBeamW = fBeamW
		self.rBeamH = rBeamH
		self.rBeamW = rBeamW
		self.colH = colH
		self.colW = colW
		self.condens = condens
		self.slabload = 1.4*(self.slabdp*self.condens+self.fhs+self.patAllw)+1.6*self.Lload
		self.beamload = 1.4*(self.rBeamH*self.rBeamW*self.condens+self.bfhs+self.wLoad*(self.wallH-self.fBeamH))
		self.beams = []
		self.Icol = (colW*colH**3)/12
		self.iRoofBeam = (rBeamW*rBeamH**3)/12
		self.cols = None
		self.kbeam5e = 1321.92*10**3
		self.kbeam5i = 1584.36*10**3
		self.kbeam6e = 1158.30*10**3
		self.kbeam6i = 1377.00*10**3
		self.roofBeamLoad = roofload
		# self.floorBeamFlangeWidth5E = 725
		# self.floorBeamFlangeWidth5I = 1225
		# self.hfh = slabdp/fBeamH

	def addcols(self,colsdict):
		self.cols = colsdict

	def floors(self,st):
		flrs = ['R']
		g = 'G'
		div = []
		fl = [st-e for e in range(1,st)]

		for e in fl:
			flrs.append(e)
		flrs.append(g)

		for e in range(len(flrs)):
			if e == len(flrs)-1:
				break
			div.append(str(flrs[e])+'-'+str(flrs[e+1]))
		return div

	def addBeams():
		for beam,btype in beamlist:
			self.beams.append(beamlist)


	def shortSpanBeam(self,x,w):
		return(1/3*w*x)

	def longSpanBeam(self,x,k,w):
		return(1/2*(1-1/(3*k**2))*w*x)

	def fixedEndM(self,w,l):
		return(1/12*l**2*w)

	def spanloadsM(self,col,st):
		for column,beams in col.items():
			print(column)
			spanM = {}
			for e in self.floors(st):
				if 'R' in e:
					load1 = self.rLoad
					load2 = self.roofBeamLoad
				else:
					load1 = self.slabload
					load2 = self.beamload
				tem = [i for i in beams]
				vals =[beams[i] for i in tem]
				# x = min(vals)
				# y = max(vals)
				# k = y/x
				if len(vals)==2:
					try:
						x = beams[1]
						y = beams[3]
						ss = min([x,y])
						ls = max([x,y])
						k = ls/ss
						ssp = self.shortSpanBeam(ss,load1)
						lsp = self.longSpanBeam(ss,k,load1)
						Mx = self.fixedEndM(ssp+load2,ss)
						My = self.fixedEndM(lsp+load2,ls)
						print(e,Mx,My)
					except:
						try:
							x = beams[0]
							y = beams[3]
							ss = min([x,y])
							ls = max([x,y])
							k = ls/ss
							ssp = self.shortSpanBeam(ss,load1)
							lsp = self.longSpanBeam(ls,k,load1)
							Mx = self.fixedEndM(ssp+load2,ss)
							My = self.fixedEndM(lsp+load2,ls)
							print(e,Mx,My)
						except:
							try:
								x = beams[0]
								y = beams[2]
								ss = min([x,y])
								ls = max([x,y])
								k = ls/ss
								ssp = self.shortSpanBeam(ss,load1)
								lsp = self.longSpanBeam(ls,k,load1)
								Mx = self.fixedEndM(ssp+load2,ss)
								My = self.fixedEndM(lsp+load2,ls)
								print(e,Mx,My)
							except:
								try:
									x = beams[1]
									y = beams[2]
									ss = min([x,y])
									ls = max([x,y])
									k = ls/ss
									ssp = self.shortSpanBeam(ss,load1)
									lsp = self.longSpanBeam(ls,k,load1)
									Mx = self.fixedEndM(ssp+load2,ss)
									My = self.fixedEndM(lsp+load2,ls)
									print(e,Mx,My)
								except:
									print()

				elif len(vals)==3:
					try:
						sum([beams[0],beams[1],beams[2]])

						x0 =beams[0] 
						x1 =beams[1]
						y2 = beams[2]
						k0 = x0/y2
						k1 = x1/y2
						ssp = 2*self.shortSpanBeam(y2,load1)
						llsp = 2*self.longSpanBeam(x0,k0,load1)
						rlsp = 2*self.longSpanBeam(x1,k1,load1)

						My = self.fixedEndM(ssp+load2,y2)
						Mx0 = self.fixedEndM(llsp+load2,x0)
						Mx1 = self.fixedEndM(rlsp+load2,x1)
						Mx = Mx1-Mx0
						print(e,Mx,My)


					except:
						try:
							sum([beams[2],beams[3],beams[1]])
							x1 =beams[1] 
							y2 =beams[2]
							y3 = beams[3]
							k2 = y2/x1
							k3 = y3/x1
							ssp2 = 2*self.shortSpanBeam(y2,load1)
							ssp3 = 2*self.shortSpanBeam(y3,load1)

							lsp1 = (2*self.longSpanBeam(y2,k2,load1)+2*self.longSpanBeam(y3,k3,load1))/2

							Mx = self.fixedEndM(lsp1+load2,x1)
							My2 = self.fixedEndM(ssp2+load2,y2)
							My3 = self.fixedEndM(ssp3+load2,y3)
							My = My2-My3
							print(e,Mx,My)
						except:
							try:
								sum([beam[1],beam[2],beam[3]])
							except:
								try:
									sum([beam[0],beam[1],beam[3]])
								except:
									print()

				else:
					print()

				# print(e,self.fixedEndM(ssp+load2,x),self.fixedEndM(lsp+load2,y))
				# spanM[e]= self.fixedEndM(ssp),self.fixedEndM(lsp)
			# return spanM




	def calColLoad(cols,st):
		for col,vals in cols.items():
			self.spanloadsM(vals,st)






	# def addcols(columnslist):
	# 	for e in columnslist:

	# def floorbeams():
	# 	for e in self.beams:
	# 		if e[1]=='E':
	# 			return(self.longSpanBeam(e[0]*e[2]*self.slabload))
	# 		else



# print(fixedEndM(41.5,6))
fcu = 25
fy = 410
Lload = 2.5
patAllw = 1
fhs =1.2
bfhs = 1
rLoad = 1.5*1.5
roofBeamLoad = 4.9
wLoad = 3.47
wallH = 3.15
slabdp = 0.15
fBeamH = 0.6
fBeamW = 0.23
rBeamH = 0.45
rBeamW = 0.23
colH = 0.225
colW = 0.225

# lo = columnload(fcu,fy,Lload,patAllw,fhs,bfhs,rLoad,\
# 		wLoad,wallH,slabdp,fBeamH,fBeamW,rBeamH,rBeamW,\
# 		colH,colW)

# print(lo.slabload)


# print(lo.spanloadsM())
# print(lo.beamload)

# print(lo.longSpanBeam())



class columns():
	def __init__(self,columnslist):
		self.columnslist = columnslist

		self.colkeys = [i[0] for i in self.columnslist]
		self.colcoord = [i[1:] for i in self.columnslist]
		self.colzip = zip(self.colkeys,self.colcoord)
		self.colpos = dict(self.colzip)

	
	def column(self):

		bdict = {}
		for e in range(len(self.columnslist)):
			left = None
			right = None
			top = None
			bottom = None
			for f in range(len(self.columnslist)):
				if self.columnslist[e][2] == self.columnslist[f][2] and self.columnslist[e] != self.columnslist[f]:

					if self.columnslist[f][1]>self.columnslist[e][1]:
						if right == None:
							right = self.columnslist[f]
						elif right:
							if self.columnslist[f][1]<right[1]:
								right = self.columnslist[f]

					else:
						if left == None:
							left = self.columnslist[f]
						elif left:
							if self.columnslist[f][1]>left[1]:
								left = self.columnslist[f]

				if self.columnslist[e][1] == self.columnslist[f][1] and self.columnslist[e] != self.columnslist[f]:
					if self.columnslist[f][2]>self.columnslist[e][2]:
						if top == None:
							top = self.columnslist[f]
						elif top:
							if self.columnslist[f][2]<top[1]:
								top = self.columnslist[f]
					else:
						if bottom == None:
							bottom = self.columnslist[f]
						elif bottom:
							if self.columnslist[f][2]>bottom[1]:
								bottom = self.columnslist[f]

			

			
			bdict[str(self.columnslist[e][0])] = left,right,top,bottom
		
		return bdict


	# def beamlist

	def distdic(self):
		dim = self.colpos
		conn = self.column()
		conload ={}
		for k,v in conn.items():
			conload[k] = {}
			for i,e in enumerate(v):
				if e:
					conload[k][i] = ((dim[k][0]-e[1])**2 +(dim[k][1]-e[2])**2)**0.5

		return conload
		# print(conload)

	def floorarea(self):
		colarea = {}
		for ke,ve in self.distdic().items():
			tem = [i for i in ve.keys()]
			if len(ve)==2:
				floorarea = ve[tem[0]]/2*ve[tem[1]]/2
				colarea[ke]=ve,floorarea,ve[tem[0]]/2+ve[tem[1]]/2
			elif len(ve)==3:
				try:
					floorarea =(ve[0]+ve[1])/2*(ve[3])/2
					colarea[ke]=ve,floorarea,(ve[0]+ve[1])/2+(ve[3])/2
				except:
					try:
						floorarea =(ve[2]+ve[3])/2*(ve[1])/2
						colarea[ke]=ve,floorarea,(ve[2]+ve[3])/2+(ve[1])/2
					except:
						try:
							floorarea =(ve[2]+ve[3])/2*(ve[0])/2
							colarea[ke]=ve,floorarea,(ve[2]+ve[3])/2+(ve[0])/2
						except:
							try:
								floorarea =(ve[0]+ve[1])/2*(ve[2])/2
								colarea[ke]=ve,floorarea,(ve[0]+ve[1])/2+(ve[2])/2
							except:
								print()
			# elif len(ve)==4:
			# 	if ve[0]==ve[1] and ve[2]==ve[3]:
			# 		colarea[ke]=ve,floorarea
		return colarea




columnslist = [
('A1',0,0),('A2',6,0),('A3',12,0),('A4',18,0),
('B1',0,-5),('B2',6,-5),('B3',12,-5),('B4',18,-5),
('C1',0,-10),('C2',6,-10),('C3',12,-10),('C4',18,-10),
('D1',0,-15),('D2',6,-15),('D3',12,-15),('D4',18,-15)
]




lo = columnload(fcu,fy,Lload,patAllw,fhs,bfhs,rLoad,\
		wLoad,wallH,slabdp,fBeamH,fBeamW,rBeamH,rBeamW,\
		colH,colW,roofBeamLoad)


ups = columns(columnslist)
# print(ups.colpos)

cos = ups.floorarea()
loading = ups.distdic()

print(loading)
print(lo.spanloadsM(loading,4))

# print(cos)
# def colload(roofload,beamload,col,sla,wal,colarea):
# 	for k,v in colarea.items():
# 		print('Column',k)
# 		print('Second Floor - Roof Level:')
# 		roof = roofload*v[1]
# 		beam = beamload*v[2]
# 		print('Roof load =', roof)
# 		print('Roof beam =', beam)  
# 		print('Column own =', col)
# 		print('Total =', roof+beam+col)
# 		print()
# 		print('First Floor - Second Floor Level:')
# 		above = roof+beam+col

# 		slab = sla*v[1]
# 		wall = wal*v[2]
# 		print('Loading above =', above)
# 		print('Slab load =', slab)  
# 		print('wall/beam load =', wall)
# 		print('column own =', col)
# 		print('Total',above+slab+wall+col)
# 		above1 = above+slab+wall+col
# 		print()
# 		print('Ground - First floor Level:')

# 		print('Loading above =',above1)
# 		print('Slab load =', slab)  
# 		print('wall/beam load =', wall)
# 		print('column own =', col)
# 		print('Total',above1+slab+wall+col)

# 		print()
# 		print()



# colload(1.5*1.5,3.484*1.4,10,12.5,17.5,cos)














	# elif len(vals)==3:
	# 	try:
	# 		sum([beams[0],beams[1],beams[2]])


	# 		if beams[0]>beams[2] and beams[1]>beams[2]:

	# 			x0 =beams[0] 
	# 			x1 =beams[1]
	# 			y = beams[2]
	# 			k0 = x0/y
	# 			k1 = x1/y
	# 			ssp = 2*self.shortSpanBeam(x2,load1)
	# 			llsp = 2*self.longSpanBeam(x0,k0,load1)
	# 			rlsp = 2*self.longSpanBeam(x1,k1,load1)

	# 			Mx = self.fixedEndM(ssp+load2,y)
	# 			My0 = self.fixedEndM(lsp+load2,x0)
	# 			My1 = self.fixedEndM(lsp+load2,x1)
	# 			My = My1-My0
	# 			print(e,My,Mx)

	# 		else:
	# 			x0 =beams[0] 
	# 			x1 =beams[1]
	# 			y = beams[2]
	# 			k0 = y/x0
	# 			k1 = y/x1
	# 			lssp = 2*self.shortSpanBeam(x0,load1)
	# 			rssp = 2*self.shortSpanBeam(x1,load1)

	# 			llsp = (2*self.longSpanBeam(x0,k0,load1)+2*self.longSpanBeam(x1,k,load1))/2

	# 			My = self.fixedEndM(llsp+load2,y)
	# 			Mx0 = self.fixedEndM(lssp+load2,x0)
	# 			Mx1 = self.fixedEndM(rssp+load2,x1)
	# 			Mx = Mx1-Mx0
	# 			print(e,Mx,My)


	# 	except:
	# 		try:
	# 			sum([beams[2],beams[3],beams[1]])
	# 			if beams[1]>beams[2] and beams[1]>beams[3]:

	# 				x2 =beams[2] 
	# 				x3 =beams[3]
	# 				x1 = beams[1]
	# 				k2 = x1/x2
	# 				k3 = x1/x3
	# 				ssp = 2*self.shortSpanBeam(x2,load1)
	# 				llsp = 2*self.longSpanBeam(x0,k0,load1)
	# 				rlsp = 2*self.longSpanBeam(x1,k1,load1)

	# 				Mx = self.fixedEndM(ssp+load2,y)
	# 				My0 = self.fixedEndM(lsp+load2,x0)
	# 				My1 = self.fixedEndM(lsp+load2,x1)
	# 				My = My1-My0
	# 				print(e,My,Mx)

	# 			else:
	# 				x0 =beams[0] 
	# 				x1 =beams[1]
	# 				y = beams[2]
	# 				k0 = y/x0
	# 				k1 = y/x1
	# 				lssp = 2*self.shortSpanBeam(x0,load1)
	# 				rssp = 2*self.shortSpanBeam(x1,load1)

	# 				llsp = (2*self.longSpanBeam(x0,k0,load1)+2*self.longSpanBeam(x1,k,load1))/2

	# 				My = self.fixedEndM(llsp+load2,y)
	# 				Mx0 = self.fixedEndM(lssp+load2,x0)
	# 				Mx1 = self.fixedEndM(rssp+load2,x1)
	# 				Mx = Mx1-Mx0
	# 				print(e,Mx,My)
	# 		except:
	# 			try:
	# 				sum([beam[1],beam[2],beam[3]])
	# 			except:
	# 				try:
	# 					sum([beam[0],beam[1],beam[3]])
	# 				except:
	# 					print()

	# else:
	# 	print()

