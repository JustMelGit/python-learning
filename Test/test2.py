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
# 		return str(self.value)

# n5 = binaryTree(5)
# n2 = binaryTree(2)
# n1 = binaryTree(1)
# n4 = binaryTree(4)
# n8 = binaryTree(8)
# n6 = binaryTree(6)
# n7 = binaryTree(7)
# n3 = binaryTree(3)
# n5.setLeftBranch(n2)
# n2.setParent(n5)
# n5.setRightBranch(n8)
# n8.setParent(n5)
# n2.setLeftBranch(n1)
# n1.setParent(n2)
# n2.setRightBranch(n4)
# n4.setParent(n2)
# n8.setLeftBranch(n6)
# n6.setParent(n8)
# n6.setRightBranch(n7)
# n7.setParent(n6)
# n4.setLeftBranch(n3)
# n3.setParent(n4)

# def leaf(node):
# 	return not node.getLeftBranch() and not node.getRightBranch()

# def TracePath(node):
# 	if not node.getParent():
# 		return[node]
# 	else:
# 		return[node] + TracePath(node.getParent())

# def BFSBinary(root, fcn):
# 	pathList = {}
# 	n = 0
# 	queue = [root]
# 	while len(queue) > 0:
# 		# print('at',queue[0])
# 		if fcn(queue[0]):
# 			n+=1
# 			newpath = TracePath(queue[0])
# 			# print('newpath',[e for e in newpath])

# 			pathList[n]=newpath[::-1]
# 			popped = queue.pop(0)
# 			# print('popped', popped)
# 		else:
# 			temp = queue.pop(0)
# 			if temp.getLeftBranch():
# 				queue.append(temp.getLeftBranch())
# 			if temp.getRightBranch():
# 				queue.append(temp.getRightBranch())
# 	return pathList

# def treeHeight(startNode):
# 	if startNode == None:
# 		return 0
# 	else:
# 		lHeight = treeHeight(startNode.getLeftBranch())
# 		rHeight = treeHeight(startNode.getRightBranch())
# 		if lHeight>rHeight:
# 			height = lHeight+1
# 		else:
# 			height = rHeight+1
# 	return height

# def treeTrans(node,level):
# 	# print('level',level)
# 	# print(node)
# 	nodes = []
# 	if node==None:
# 		return
# 	if level==1:
# 		print(node)
# 		nodes.append(node)

# 		return nodes
# 		# print('nodes', nodes)
# 	elif level>1:
# 		treeTrans(node.getLeftBranch(),level-1)
# 		treeTrans(node.getRightBranch(),level-1)
# 	# return nodes

# def treeTrans(node,level):
# 	# print('level',level)
# 	# print(node)
# 	nodes = []
# 	if node==None:
# 		print('none ',node)
# 		return
# 	if level==1:
# 		print(node)
# 		nodes.append(node)
# 		print('nodes',nodes)
# 		return nodes
# 		# print('nodes', nodes)
# 	elif level>1:
# 		treeTrans(node.getLeftBranch(),level-1)
# 		treeTrans(node.getRightBranch(),level-1)
# 	# return nodes


# def printTree(root):
# 	nodeslist = {}
# 	h = treeHeight(root)
# 	for i in range(1,h+1):
# 		g = treeTrans(root,i)
# 		nodeslist[i] = g
# 	return nodeslist

# print(printTree(n5))


# class myQueue():
#     def __init__(self):
#         self.items = []

#     def addItems(self,item):
#         self.items.append(item)

#     def nextItem(self):
#         temp = self.items.pop(0)
#         self.items.append(temp)
#         return temp

# persons = ['mel', 'cour', 'faith', 'harvest', 'havillah', \
# 'blessing', 'shellar', 'endy', \
# 'amaka', 'rejoice', 'ebere', 'jumoke', 'Ada', \
# 'Tolu', 'Yemisi', 'Omo','harvest']

# persons_queue = myQueue()

# for e in persons:
# 	persons_queue.addItems(e)


# def conflict(i,item, students,assistant):
# 	if i == 0:
# 		templist = students[0]+students[1]
# 	elif i ==len(students)-1:
# 		templist = assistant[i-1]+assistant+students[i]+students[i-1]
# 	else:
# 		templist = students[i-1]+assistant[i-1]+students[i]+students[i+1]

# 	return item in templist


# weeksStudents = [['mel','cour','faith'],['harvest','havillah','blessing'],['shellar','endy','amaka']]
# partners = []


# for i in range(len(weeksStudents)):
# 	partners.append([])
# 	while len(partners[i])<len(weeksStudents[i]):
# 		person = persons_queue.nextItem()
# 		if not conflict(i,person,weeksStudents,partners):
# 			partners[i].append(person)
# print(partners)

# def assistants(i,students,assistant):
# 	for person in persons:
# 		if not conflict(i,person,students,assistant):
# 			if len(assistant)==len(students[i]):
# 				yield [person]
# 	else:
# 		for result in assistants(i,students,assistant+person):
# 			yield [person] + result

# print(assistants(0,weeksStudents,partners))

