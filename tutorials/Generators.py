# def flatten(nested):
# 	try:
# 		for sublist in nested:
# 			for element in flatten(sublist):
# 				yield element
# 	except TypeError:
# 		yield nested

# # print(list(flatten([[[1],2],3,4,[5,[6,7]],8])))

# def flatten(nested):
# 	try:
# 		try:
# 			nested + ''
# 		except TypeError: pass
# 		else: raise TypeError
# 		for sublist in nested:
# 			for element in flatten(sublist):
# 				yield element
# 	except TypeError:
# 		yield nested
# print(list(flatten(["hello, world"])))
# print(list(flatten([1,2,[3,4],'world'])))


# def conflict(state, nextX):
# 	nextY = len(state)
# 	for i in range(nextY):
# 		if abs(state[i] - nextX) in (0, nextY - i):
# 			return True
# 	return False

# def queens(num, state):
# 	if len(state) == num - 1:
# 		for pos in range(num):
# 			if not conflict(state, pos):
# 				yield pos

# def queens(num=8, state=()):
# 	for pos in range(num):
# 		if not conflict(state, pos):
# 			if len(state) == num-1:
# 				yield(pos,)
# 			else:
# 				for result in queens(num, state + (pos,)):
# 					yield (pos,) + result
# print(list(queens(8, ())))




# def permutation_generator(word):
# 	print('calling permutation_generator with',word)
# 	if len(word)==1:
# 		yield (word[0],)
# 	else:
# 		for m in range(len(word)):
# 			# print(m)
# 			for n in permutation_generator(word[:m] + word[m+1:]):
# 				print('results',list(n))
# 				yield (word[m],) + n


# Animals = ['cat','kit','fox','cow']
# Animalss = ['cat','kite','fox']
# Sisters = ['cour']
# sis = []
# nu = [1,2,3,4]





# for m in range(len(Animals)):
# 	print('first',Animals[:m],'second',Animals[m+1:])






# for x in permutation_generator(Animals):
# 	print(x)

# def genT(lists):
# 	if len(lists)==1:
# 		yield (lists[0],)
# 	else:
# 		for m in range(len(lists)):
# 			for n in genT(lists[:m]+lists[m+1:]):
# 				yield (lists[m],) + n 


# x = genT(nu)
# for e in x:
# 	print(e)

# class person():
# 	def __init__(self,name,sex):
# 		self.name = name
# 		self.sex = sex

# 	def getname(self):
# 		return self.name

# 	def getsex(self):
# 		return self.sex


# jw = person('Jahswill','male')
# st = person('Stella','female')
# th = person('Theodore','male')
# dv = person('Divine','female')
# lj = person('lovejah','female')
# fa = person('favor','female')


# def conflict(state,roomy):
# 	if state.getsex()=='female' and roomy.getsex()=='male':
# 		return True
# 	elif state.getsex()=='male' and roomy.getsex()=='female':
# 		return True
# 	else:
# 		return False

# persons = [jw,st,th,dv,lj,fa]

# def rooming(state,persons):
# 	for person in persons:
# 		if not conflict(state,person):
# 			yield(person.getname())


# print(list(rooming(jw,persons)))




# lis = ['ja','mel','gil','ja']
# for e in lis:
# 	if lis.count(e)==2:
# 		do = e
# print(do)
# print(lis.count('ja'))

# g= {1: 6.0, 3: 5.0}

# lt = g.keys()

# for e in lt:
# 	print(e)

# def floors(st):
# 	st = 3
# 	flrs = ['R']
# 	g = 'G'
# 	div = []
# 	fl = [st-e for e in range(1,st)]

# 	for e in fl:
# 		flrs.append(e)
# 	flrs.append(g)

# 	for e in range(len(flrs)):
# 		if e == len(flrs)-1:
# 			break
# 		div.append((flrs[e],flrs[e+1]))
# 	return div

# print(floors(4))

# if len(ls)==2:
# 	print(ls[0],'-',ls[1])

# for e in range(1,st):
	
# 	print(st-e)

# def conflict(state, nextX):
# 	nextY = len(state)
# 	for i in range(nextY):

# 		if (state[i-1]==nextX):

# 			return True
# 	return False

# def queens(lecturers, state):
	

# 		for lecturer in lecturers:
# 			if not conflict(state, lecturer):
# 				if len(state) == len(lecturers) - 1:

# 					yield (lecturer,)
# 				else:
# 					for result in queens(lecturers,state+(lecturer,)):
# 						yield (lecturer,)+result



# Pti_lecturers = ['Jewo','David','Uwan','Akusu','Ese','Shedi','Haruna','Joseph']


# for e in queens(Pti_lecturers,()):
# 	print(e)

# def conflict(state, nextX):
# 	nextY = len(state)
# 	for i in range(nextY):
# 		if abs(state[i] - nextX) in (0, nextY - i):
# 			return True
# 	return False

# def queens(num, state):
# 	if len(state) == num - 1:
# 		for pos in range(num):
# 			if not conflict(state, pos):
# 				yield pos

# def queens(num=8, state=()):
# 	for pos in range(num):
# 		if not conflict(state, pos):
# 			if len(state) == num-1:
# 				yield(pos,)
# 			else:
# 				for result in queens(num, state + (pos,)):
# 					yield (pos,) + result
# print(list(queens(8, ())))



# import websocket
# SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

# def on_open(ws):
# 	print('opened connection')

# def on_close(ws):
# 	print('closed connection')

# def on_message(ws,message):
# 	print('received message')
# 	print(message)

# ws = websocket.WebSocketApp(SOCKET, on_open=on_open,on_close = on_close, on_message = on_message)
# ws.run_forever()

# Python program to explain os.urandom() method 
          
# importing os module 
# import os 
      
# # Declaring size
# size = 5
  
# # Using os.urandom() method
# result = os.urandom(size).hex() 
      
# # Print the random bytes string
# # Output will be different everytime
# print(result)


# def kinetic_energy(m:'in KG', v:'in M/S')->'Joules': 
#     return 1/2*m*v**2


# print(kinetic_energy(5,6))
 
# print(kinetic_energy.__annotations__)
# import itertools as it
# for _ in it.repeat(None, 5):
# 	print('yes')



