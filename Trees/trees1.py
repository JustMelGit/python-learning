class binaryTree():
	def __init__(self,value):
		self.value = value
		self.leftBranch = None
		self.rightBranch = None
		self.parent = None

	def setLeftBranch(self,node):
		self.leftBranch = node

	def setRightBranch(self,node):
		self.rightBranch = node

	def setParent(self,node):
		self.parent = node

	def getLeftBranch(self):
		return self.leftBranch

	def getRightBranch(self):
		return self.rightBranch

	def getParent(self):
		return self.parent

	def getValue(self):
		return self.value

	def __str__(self):
		return str(self.value)


n5 = binaryTree(5)
n4 = binaryTree(4)
n2 = binaryTree(2)
n3 = binaryTree(3)
n1 = binaryTree(1)
n7 = binaryTree(7)
n6 = binaryTree(6)
n8 = binaryTree(8)

n5.setLeftBranch(n4)
n5.setRightBranch(n6)
n4.setLeftBranch(n2)
n4.setRightBranch(n3)
n4.setParent(n5)
n6.setParent(n5)
n2.setLeftBranch(n1)
n2.setParent(n4)
n3.setParent(n4)
n6.setRightBranch(n7)
n1.setParent(n2)
n7.setParent(n6)


# def DFS(root,goal):
# 	stack = [root]
# 	while len(stack) != 0:
# 		temp = stack.pop(0)
# 		if temp == goal:
# 			return True
# 		if temp.getRightBranch():
# 			stack.insert(0,temp.getRightBranch())
# 		if temp.getLeftBranch():
# 			stack.insert(0,temp.getLeftBranch())
# 	return False

# # print(DFS(n5,n4))

# def BFS(root,goal):
# 	queue = [root]
# 	while len(queue)!=0:
# 		temp = queue.pop(0)
# 		if temp == goal:
# 			return True
# 		if temp.getLeftBranch():
# 			queue.append(temp.getLeftBranch())
# 		if temp.getRightBranch():
# 			queue.append(temp.getRightBranch())
# 	return False

# # print(BFS(n5,n2))

# def tracePath(node):
# 	if not node.getParent():
# 		return node
# 	else:
# 		return str(node) + '-' + str(tracePath(node.getParent()))

# def BFSWITHPATH(root,goal):
# 	queue = [root]
# 	while len(queue)!=0:
# 		temp = queue.pop(0)
# 		if temp == goal:
# 			return tracePath(temp)
# 		if temp.getLeftBranch():
# 			queue.append(temp.getLeftBranch())
# 		if temp.getRightBranch():
# 			queue.append(temp.getRightBranch())
# 	return False

# print(BFSWITHPATH(n5,n2))

# def LtFun(goal,node):
# 	return goal.value < node.value

# print(LtFun(n3,n5))

# def DFSORDERD(root,goal):
# 	stack = [root]
# 	while len(stack)!=0:
# 		temp = stack.pop(0)
# 		print(temp)
# 		if temp == goal:
# 			return True
		
# 		if LtFun(goal,temp):

# 			if temp.getLeftBranch():
# 				stack.insert(0,temp.getLeftBranch())
# 		else:
# 			if temp.getRightBranch():
# 				stack.insert(0,temp.getRightBranch())

# 	return False

# print(DFSORDERD(n5,n1))

# def treeEle(node):
# 	if node.getLeftBranch()==None:
# 		return 0
# 	else:
# 		return 1 + treeEle(node.getLeftBranch())

# print(treeEle(n5))


# def printLeft(h,n):
# 	if h == 1:
# 		print(n.getLeftBranch())
# 	else:
# 		printLeft(h-1,n.getLeftBranch())

# print(printLeft(3,n5))


def heightTree(node):
	if node == None:
		return 0
	lheight = heightTree(node.getLeftBranch())
	rheight = heightTree(node.getRightBranch())
	if lheight>rheight:
		height = lheight+1
	else:
		height = rheight+1
	return height


def printCurrentLevel(node,level):
	if node == None:
		return None
	if node != None:
		if level == 1:
			if sum(node.getValue()) == 8:
				print(node)
		else:
			printCurrentLevel(node.getLeftBranch(),level-1)
			printCurrentLevel(node.getRightBranch(),level-1)


# # print(printTree(n5))

def printTreeList(aTree):
	for e in aTree:
		if not isinstance(e,list):
			print(e)
		else:
			printTreeList(e)

# printTreeList(printTree(n5))


def width(node,level):
	if node == None:
		return 0
	if level == 1:
		return 1
	else:
		return (width(node.getLeftBranch(),level-1) +
		width(node.getRightBranch(),level-1))


def maxWidthTree(node):
	maxwidth = 0
	h = heightTree(node)
	for i in range(1,h+1):
		w = width(node,i)
		if maxwidth < w:
			maxwidth = w
	return maxwidth

# print(printTree(n5))


def count(root):
	if root == None:
		return 0
	else:
		left = 1 + count(root.getLeftBranch())
		right = 1 + count(root.getRightBranch())
	return left+right

print(count(n5))










# def implicitTree(sofar, todo):
# 	if len(todo) == 0:
# 		return binaryTree(sofar)
	
# 	else:
# 		toTake = implicitTree(sofar+[todo[0]],todo[1:])
# 		without = implicitTree(sofar,todo[1:])
# 		here = binaryTree(sofar)
# 		here.setLeftBranch(toTake)
# 		here.setRightBranch(without)
# 	return here


# a = [6,3]
# b = [7,2]
# c = [8,4]
# d = [9,5]
# lst = [a,b,c,d]

# treeTest = implicitTree([], [a,b,c,d])



# print(heightTree(treeTest))
# print(maxWidthTree(treeTest))


# def printTree(node):
# 	h = heightTree(node)
# 	for i in range(1,h+1):
# 		printCurrentLevel(node,i)
# # printTree(treeTest)

# def maxVal(someLists):
# 	# print(someLists)
# 	lsts = [e[1] for e in someLists.value]
# 	return sum(lsts)

# print(maxVal(lst))


# def DFSTREEMAX(root,constraint):
# 	stack = [root]
# 	maxV = None
# 	node = None
# 	while len(stack) != 0:
# 		# print(node,maxV)
# 		temp = stack.pop(0)
# 		if not maxV and maxVal(temp)<constraint:
# 			maxV = maxVal(temp)
# 			node = temp
# 		elif maxVal(temp)>maxV and maxVal(temp)<constraint:
# 			maxV = maxVal(temp)
# 			node = temp
# 		if temp.getRightBranch():
# 			stack.insert(0,temp.getRightBranch())
# 		if temp.getLeftBranch():
# 			stack.insert(0,temp.getLeftBranch())
# 	return node.value,maxV

# print(DFSTREEMAX(treeTest,14))

 
# def implicit(todo,available):
# 	print(todo)
# 	if todo == [] or available == 0:
# 		result = 0,()
# 		return result

# 	elif todo[0][1]>available:
# 		result = implicit(todo[1:],available)

# 	else:
# 		nextItem = todo[0]
# 		withToTakeValue,withToTakeList = implicit(todo[1:],available-nextItem[1])
# 		withToTakeValue += nextItem[0]
# 		withToTakeList += (nextItem,)

# 		withoutToTakeValue,withoutToTakeList = implicit(todo[1:],available)
		
# 		if withToTakeValue>withoutToTakeValue:
# 			result = withToTakeValue,withToTakeList
# 		else:
# 			result = withoutToTakeValue,withoutToTakeList
# 	return result

# # a = [6,3]
# # b = [7,2]
# # c = [8,4]
# # d = [9,5]

# c = [175,10]
# p = [90,9]
# r = [20,4]
# v = [10,1]
# co = [200,20]



# # lst = [a,b,c,d]
# lst1 = [c,p,r,v,co]
# print(implicit(lst1,20))



def implicitTree(sofar,n):
	if n == 0:
		return binaryTree(sofar)
	
	else:
		oneStep = implicitTree(sofar+[1],n-1)
		twoStep = implicitTree(sofar+ [2],n-1)
		here = binaryTree(sofar)
		here.setLeftBranch(oneStep)
		here.setRightBranch(twoStep)
	return here


treeTest = implicitTree([],8)

# print(heightTree(treeTest))

def printTree(node):
	h = heightTree(node)
	for i in range(1,h+1):
		printCurrentLevel(node,i)

# printTree(treeTest)
# print(maxWidthTree(treeTest))




