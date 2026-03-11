class binaryTree(object):
	def __init__(self, value):
		self.value = value
		self.leftBranch = None
		self.rightBranch = None
		self.parent = None
	def setLeftBranch(self, node):
		self.leftBranch = node
	def setRightBranch(self, node):
		self.rightBranch = node
	def setParent(self, parent):
		self.parent = parent
	def getValue(self):
		return self.value
	def getLeftBranch(self):
		return self.leftBranch
	def getRightBranch(self):
		return self.rightBranch
	def getParent(self):
		return self.parent
	def __str__(self):
		return (self.value)

n5 = binaryTree(5)
n2 = binaryTree(2)
n1 = binaryTree(1)
n4 = binaryTree(4)
n8 = binaryTree(8)
n6 = binaryTree(6)
n7 = binaryTree(7)
n5.setLeftBranch(n2)
n2.setParent(n5)
n5.setRightBranch(n8)
n8.setParent(n5)
n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
n8.setLeftBranch(n6)
n6.setParent(n8)
n6.setRightBranch(n7)
n7.setParent(n6)



def find6(node):
	return node.getValue() == 6

def lt6(node):
	return node.getValue() > 6

def DFSBinary(root, fcn):
	stack = [root]
	while len(stack) > 0:
		if fcn(stack[0]):
			return True
		else:
			temp = stack.pop(0)
		if temp.getRightBranch():
			stack.insert(0, temp.getRightBranch())
		if temp.getLeftBranch():
			stack.insert(0, temp.getLeftBranch())
	return False

print(DFSBinary(n5, find6))

def BFSBinary(root):
	queue = [root]
	while len(queue) > 0:
		if find6(queue[0]):
			return True
		else:
			temp = queue.pop(0)
		if temp.getLeftBranch():
			queue.append(temp.getLeftBranch())
		if temp.getRightBranch():
			queue.append(temp.getRightBranch())
	return False

print(BFSBinary(n6))

def BFSBinary(root, fcn):
	queue = [root]
	while len(queue) > 0:
		if fcn(queue[0]):
			return True
		else:
			temp = queue.pop(0)
		if temp.getLeftBranch():
			queue.append(temp.getLeftBranch())
		if temp.getRightBranch():
			queue.append(temp.getRightBranch())
	return False

print(BFSBinary(n5,find6))

def TracePath(node):
	if not node.getParent():
		return[node]
	else:
		return[node] + TracePath(node.getParent())


def DFSBinaryPath(root, fcn):
	stack = [root]
	while len(stack) > 0:
		if fcn(stack[0]):
			return TracePath(stack[0])
		else:
			temp = stack.pop(0)
			if temp.getRightBranch():
				stack.insert(0, temp.getRightBranch())
			if temp.getLeftBranch():
				stack.insert(0, temp.getLeftBranch())
	return False


foo = DFSBinaryPath(n5,find6)
print([e.getValue() for e in foo])


for e in foo:
	print(e.getValue())


foo = print(DFSBinaryPath(n5,find6))


def DFSBinaryOrdered(root, fcn, ltFcn):
	stack = [root]
	while len(stack) > 0:
		if fcn(stack[0]):
			return True
		elif ltFcn(stack[0]):
			temp = stack.pop(0)
		if temp.getLeftBranch():
			stack.insert(0, temp.getLeftBranch())
		else:
			if temp.getRightBranch():
				stack.insert(0, temp.getRightBranch())
	return False



def BFSDTree(root, valueFcn, constraintFcn):
	queue = [root]
	best = None
	visited = 0
	while len(queue) > 0:
		visited += 1
	if constraintFcn(queue[0].getValue()):
		if best == None:
			best = queue[0]
	elif valueFcn(queue[0].getValue()) > valueFcn(best.getValue()):
		best = queue[0]
	temp = queue.pop(0)
	if temp.getLeftBranch():
		queue.append(temp.getLeftBranch())
	if temp.getRightBranch():
		queue.append(temp.getRightBranch())
	else:
		queue.pop(0)
	print('visited', visited)
	return best



def buildDTree(sofar, todo):
	if len(todo) == 0:
		return binaryTree(sofar)
	else:
		withelt = buildDTree(sofar + [todo[0]], todo[1:])
		withoutelt = buildDTree(sofar, todo[1:])
		here = binaryTree(sofar)
		here.setLeftBranch(withelt)
		here.setRightBranch(withoutelt)
	return here

def DFSDTree(root, valueFcn, constraintFcn):
	stack = [root]
	best = None
	visited = 0
	while len(stack) > 0:
		visited += 1
		if constraintFcn(stack[0].getValue()):
			if best == None:
				best = stack[0]
			elif valueFcn(stack[0].getValue()) > valueFcn(best.getValue()):
				best = stack[0]
			temp = stack.pop(0)
			if temp.getRightBranch():
				stack.insert(0, temp.getRightBranch())
			if temp.getLeftBranch():
				stack.insert(0, temp.getLeftBranch())
		else:
			stack.pop(0)

	print ('visited', visited)
	return best

a = [6,3]
b = [7,2]
c = [8,4]
d = [9,5]
# lst = [a,b,c,d]

treeTest = buildDTree([], [a,b,c,d])


def sumValues(lst):
	vals = [e[0] for e in lst]
	return sum(vals)

def WeightsBelow10(lst):
	wts = [e[1] for e in lst]
	return sum(wts) <= 10


foo = DFSDTree(treeTest,sumValues,WeightsBelow10)
print(foo.getValue())


BFSDTree(treeTest, sumValues, WeightsBelow10)

def DFSDTreeGoodEnough(root, valueFcn, constraintFcn, stop):
	stack = [root]
	best = None
	visited = 0
	while len(stack) > 0:
		visited += 1
		if constraintFcn(stack[0].getValue()):
			if best == None:
				best = stack[0]
		elif valueFcn(stack[0].getValue()) > valueFcn(best.getValue()):
			best = stack[0]
		if stop(best.getValue()):
			return best
		temp = stack.pop(0)
		if temp.getRightBranch():
			queue.insert(0, temp.getRightBranch())
		if temp.getLeftBranch():
			queue.insert(0, temp.getLeftBranch())
		else:
			stack.pop(0)
		print ('visited', visited)
	return best

def BFSDTreeGoodEnough(root, valueFcn, constraintFcn, stop):
	queue = [root]
	best = None
	visited = 0
	while len(queue) > 0:
		visited += 1
		if constraintFcn(queue[0].getValue()):
			if best == None:
				best = queue[0]
		elif valueFcn(queue[0].getValue()) > valueFcn(best.getValue()):
			best = queue[0]
		if stop(best.getValue()):
			return best
		temp = queue.pop(0)
		if temp.getLeftBranch():
			queue.append(temp.getLeftBranch())
		if temp.getRightBranch():
			queue.append(temp.getRightBranch())
		else:
			queue.pop(0)
		print ('visited', visited)
	return best


def atLeast15(lst):
	return sumValues(lst) >= 15
print ('DFS')

depth = DFSDTreeGoodEnough(treeTest, sumValues, WeightsBelow10, atLeast15)
print ('BFS')
breadth = BFSDTreeGoodEnough(treeTest, sumValues, WeightsBelow10, atLeast15)


def DTImplicit(toConsider, avail):
	# return value of solution, and solution
	if toConsider == [] or avail == 0:
		result = (0, ())                                 
	elif toConsider[0][1] > avail:
		result = DTImplicit(toConsider[1:], avail)
	else:
		nextItem = toConsider[0]
		withVal, withToTake = DTImplicit(toConsider[1:], avail -nextItem[1])
		withVal += nextItem[0]
		withoutVal, withoutToTake = DTImplicit(toConsider[1:], avail)
		if withVal > withoutVal:
			result = (withVal, withToTake + (nextItem,))
		else:
			result = (withoutVal, withoutToTake)
		return result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

def DFSBinaryNoLoop(root, fcn):
	stack = [root]
	seen = []
	while len(stack) > 0:
		print ('at node ' + str(queue[0].getValue()))
	if fcn(stack[0]):
		return True
	else:
		temp = stack.pop(0)         
	seen.append(temp)
	if temp.getRightBranch():
		if not temp.getRightBranch() in seen:
			stack.insert(0, temp.getRightBranch())
	if temp.getLeftBranch():
		if not temp.getLeftBranch() in seen:
			stack.insert(0, temp.getLeftBranch())
	return False