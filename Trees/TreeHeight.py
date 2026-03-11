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
		return (str(self.value))

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

# print(DFSBinary(n5, find6))

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

# print(BFSBinary(n6))

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

# print(BFSBinary(n5,find6))

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


# foo = DFSBinaryPath(n5,find6)
# print([e.getValue() for e in foo])


# for e in foo:
# 	print(e.getValue())


# foo = print(DFSBinaryPath(n5,find6))


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
# c = [8,4]
# d = [9,5]
lst = [a,b]

treeTest = buildDTree([], [a,b])


def printLevelOrder(root):
	h = height(root)
	for i in range(1, h+1):
		printCurrentLevel(root, i)

# Print nodes at a current level
def printCurrentLevel(root, level):
	if root is None:
		return
	if level == 1:
		print(root, end='\n')
	elif level > 1:
		printCurrentLevel(root.getLeftBranch(), level-1)
		printCurrentLevel(root.getRightBranch(), level-1)

""" Compute the height of a tree--the number of nodes
	along the longest path from the root node down to
	the farthest leaf node
"""

def height(node):
	if node is None:
		return 0
	else:
		# Compute the height of each subtree
		lheight = height(node.getLeftBranch())
		rheight = height(node.getRightBranch())
		# return lheight == lheight
		# print(lheight,rheight)

		#Use the larger one
		if lheight > rheight:
			return lheight+1
		else:
			return rheight+1

		
print(height(treeTest))
# print("Level order traversal of binary tree is -")
printLevelOrder(treeTest)

