
# import math

# print(math.comb(5,2))


# def powerSet(alist):
# 	if len(alist) == 0:
# 		return [[]]
# 	else:
# 		newlist = []
# 		pSet = powerSet(alist[1:len(alist)])
# 		firstEle = [alist[0]]
# 		for el in pSet:
# 			newlist += [firstEle+el]
# 		return  newlist + pSet

# seq = [1,2,3]
# print(powerSet(seq))


# def printMove(fr,to):
# 	print('move from '+str(fr)+' to '+str(to))


# def Towers(n,fr,to,spare):
# 	if n == 1:
# 		printMove(fr,to)
# 	else:
# 		Towers(n-1,fr,spare,to)
# 		Towers(1,fr,to,spare)
# 		Towers(n-1,spare,to,fr)


# t = Towers(64,'fr','to','sp')
# print(t)



