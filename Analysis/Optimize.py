# class binaryTree(object):
# 	def __init__(self, value):
# 		self.value = value
# 		self.leftBranch = None
# 		self.rightBranch = None
# 		self.parent = None
# 	def setLeftBranch(self, node):
# 		self.leftBranch = node
# 	def setRightBranch(self, node):
# 		self.rightBranch = node
# 	def setParent(self, parent):
# 		self.parent = parent
# 	def getValue(self):
# 		return self.value
# 	def getLeftBranch(self):
# 		return self.leftBranch
# 	def getRightBranch(self):
# 		return self.rightBranch
# 	def getParent(self):
# 		return self.parent
# 	def __str__(self):
# 		return (self.value)

# def buildDTree(sofar, todo):
# 	if len(todo) == 0:
# 		return binaryTree(sofar)
# 	else:
# 		withelt = buildDTree(sofar + [todo[0]], todo[1:])
# 		withoutelt = buildDTree(sofar, todo[1:])
# 		here = binaryTree(sofar)
# 		here.setLeftBranch(withelt)
# 		here.setRightBranch(withoutelt)
# 	return here

# def DFSDTree(root, valueFcn, constraintFcn):
# 	stack = [root]
# 	best = None
# 	visited = 0
# 	while len(stack) > 0:
# 		visited += 1
# 		if constraintFcn(stack[0].getValue()):
# 			if best == None:
# 				best = stack[0]
# 			elif valueFcn(stack[0].getValue()) > valueFcn(best.getValue()):
# 				best = stack[0]
# 			temp = stack.pop(0)
# 			if temp.getRightBranch():
# 				stack.insert(0, temp.getRightBranch())
# 			if temp.getLeftBranch():
# 				stack.insert(0, temp.getLeftBranch())
# 		else:
# 			stack.pop(0)

# 	print ('visited', visited)
# 	return best


# def BFSDTree(root, valueFcn, constraintFcn):
# 	queue = [root]
# 	best = None
# 	visited = 0
# 	while len(queue) > 0:
# 		visited += 1
# 		if constraintFcn(queue[0].getValue()):
# 			if best == None:
# 				best = queue[0]
# 			elif valueFcn(queue[0].getValue()) > valueFcn(best.getValue()):
# 				best = queue[0]
# 			temp = queue.pop(0)
# 			if temp.getLeftBranch():
# 				queue.append(temp.getLeftBranch())
# 			if temp.getRightBranch():
# 				queue.append(temp.getRightBranch())
# 		else:
# 			queue.pop(0)
# 	print('visited', visited)
# 	return best


# a = [6,3]
# b = [7,2]
# c = [8,4]
# d = [9,5]
# stuff = [a,b,c,d]

# treeTest = buildDTree([], [a,b,c,d])

# def sumValues(lst):
# 	vals = [e[0] for e in lst]
# 	return sum(vals)

# def WeightsBelow10(lst):
# 	wts = [e[1] for e in lst]
# 	return sum(wts) <= 10

# foo = DFSDTree(treeTest,sumValues,WeightsBelow10)
# print(foo.getValue())

# foo1 = BFSDTree(treeTest,sumValues,WeightsBelow10)
# print(foo1.getValue())

# def DTImplicit(toConsider, avail):
# 	# return value of solution, and solution
# 	if toConsider == [] or avail == 0:
# 		result = (0, ())
# 	elif toConsider[0][1] > avail:
# 		result = DTImplicit(toConsider[1:], avail)
# 	else:
# 		nextItem = toConsider[0]
# 		withVal, withToTake = DTImplicit(toConsider[1:], avail -nextItem[1])
# 		withVal += nextItem[0]
# 		withoutVal, withoutToTake = DTImplicit(toConsider[1:], avail)
# 		if withVal > withoutVal:
# 			result = (withVal, withToTake + (nextItem,))
# 		else:
# 			result = (withoutVal, withoutToTake)
# 	return result


# val,taken = DTImplicit(stuff,10)

# print(val)
# print(taken)


sides = ('left', 'right', 'top')
# nolabels = {s: False for s in sides}
# print(nolabels)


# nolabels.update({'label%s' % s: False for s in sides})
# print(nolabels)

# print(sides[:2])

word = ['cat','kit','fox']
for m in range(len(word)):
	print(word[:m] + word[m+1:])