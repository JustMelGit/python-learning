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
n8.setRightBranch(n7)
n6.setParent(n8)
# n6.setRightBranch(n7)
n7.setParent(n8)


def treeHeight(node):
	if node == None:
		return 0
	else:
		lheight = treeHeight(node.getLeftBranch())
		rheight = treeHeight(node.getRightBranch())

		if lheight>rheight:
			height = lheight+1
		else:
			height = rheight+1
	return height

# print(treeHeight(n5))


def printLevelOrder(root):
	h = treeHeight(root)
	for i in range(1, h+1):
		printCurrentLevel(root, i)


# Print nodes at a current level
def printCurrentLevel(root, level):
	# print('le',level)
	if root is None:
		return
	if level == 1:
		print(root, end='\n')
	elif level > 1:
		printCurrentLevel(root.getLeftBranch(), level-1)
		printCurrentLevel(root.getRightBranch(), level-1)


print(printLevelOrder(n5))



