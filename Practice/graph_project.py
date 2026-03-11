class node(object):
	def __init__(self, value):
		self._value = value

	def __str__(self):
		return self._value

class edge():
	def __init__(self,source,dest):
		self._source = source
		self._dest = dest

	def get_source(self):
		return self._source

	def get_dest(self):
		return self._dest

class digraph():
	def __init__(self):
		self.edges = {}
		self.nodes = set()

	def add_nodes(self,node):
		if node in self.nodes:
			raise ValueError('Duplicate node')
		else:
			self.nodes.add(node)
			self.edges[node] = []

	def add_edge(self,edge):
		src = edge.get_source()
		des = edge.get_dest()
		if not (src in self.nodes and des in self.nodes):
			raise ValueError('Node not in graph')
		self.edges[src].append(des)

	def children_of(self,node):
		return self.edges[node]

	def has_node(self,node):
		return node in self.nodes

	def __str__(self):
		res = ''
		for k in self.edges:
			for d in self.edges[k]:
				res = res + str(k) + '->' + str(d) + '\n'
		return res[:-1]


na = node('a')
nb = node('b')
nc = node('c')
nd = node('d')
ne = node('e')

g = digraph()
nodes = [na,nb,nc,nd]

e1 = edge(na,nb)
e2 = edge(na,nc)
e3 = edge(nb,nd)
e4 = edge(nc,nd)

edges = [e1,e2,e3,e4]

for node in nodes:
	g.add_nodes(node)

for edge in edges:
	g.add_edge(edge)

# print(g)

def getPaths(graph,start_node,goal_node):

	paths = []

	def printPath(path):
		res = str(path[0])
		for e in path[1:]:
			res = res + '->' + str(e)
		print(res)


	def DFS(graph,start_node,goal_node,path = [],shortest = None):
		path = path + [start_node]
		# path.append(start_node)
		print('current DFS path',end=', ')
		printPath(path)
		if start_node == goal_node:
			return path
		for child in graph.children_of(start_node):
			if child not in path:

				result = DFS(graph,child,goal_node,path,shortest)
				if result != None:
					paths.append(result)
					# shortest = result
					# return result

	DFS(graph,start_node,goal_node)
	return paths


for i,e in enumerate(getPaths(g,na,nd)):
	print()
	print(i)
	# print()
	for node in e:
		print(node)

# def printPath(path):
# 	res = str(path[0])
# 	for e in path[1:]:
# 		res = res + '->' + str(e)
# 	print(res)



# def DFS(graph,start_node,goal_node,path = [],shortest = None):
# 	path = path + [start_node]
# 	# path.append(start_node)
# 	print('current DFS path',end=', ')
# 	printPath(path)
# 	if start_node == goal_node:
# 		return path
# 	for child in graph.children_of(start_node):
# 		if child not in path:

# 			result = DFS(graph,child,goal_node,path,shortest)
# 			if result != None:
# 				# shortest = result
# 				return result



# print(DFS(g,na,nd))
# for e in DFS(g,na,nd):
	# for i in e:
	# 	print(i)
	# print(e)

# def DFS(graph,start_node,goal_node,path = [],shortest = None):
# 	path = path + [start_node]
# 	print('current DFS path',end=', ')
# 	printPath(path)
# 	if start_node == goal_node:
# 		return path
# 	for child in graph.children_of(start_node):
# 		if child not in path:

# 			result = DFS(graph,child,goal_node,path,shortest)
# 			if result != None:
# 				if not shortest:
# 					shortest = result
				
# 				elif len(result) < len(shortest):
# 					shortest = result

# 	return shortest

# for e in DFS(g,na,nd):
# 	print(e)





# def BFS(graph,start_node,goal_node,path = [], shortest = None):