
# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
import sys


class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]
		# print(self.graph)

	def printSolution(self, dist):
		print("Vertex \tDistance from Source")
		for node in range(self.V):
			print(node, "\t", dist[node])

	# A utility function to find the vertex with
	# minimum distance value, from the set of vertices
	# not yet included in shortest path tree
	def minDistance(self, dist, sptSet):

		# Initialize minimum distance for next node
		min = sys.maxsize
		# print(min)
		# return

		# Search not nearest vertex not in the
		# shortest path tree
		for u in range(self.V):
			# print(u)
			# print('new_min',min)
			if dist[u] < min and sptSet[u] == False:
				min = dist[u]
				min_index = u

		# print(min_index)
		return min_index

	# Function that implements Dijkstra's single source
	# shortest path algorithm for a graph represented
	# using adjacency matrix representation
	def dijkstra(self, src):

		dist = [sys.maxsize] * self.V
		dist[src] = 0
		print(dist)
		# return
		sptSet = [False] * self.V

		for cout in range(self.V):

			# Pick the minimum distance vertex from
			# the set of vertices not yet processed.
			# x is always equal to src in first iteration
			x = self.minDistance(dist, sptSet)
			print('x',x)
			# return

			# Put the minimum distance vertex in the
			# shortest path tree
			sptSet[x] = True

			# Update dist value of the adjacent vertices
			# of the picked vertex only if the current
			# distance is greater than new distance and
			# the vertex in not in the shortest path tree
			for y in range(self.V):
				if self.graph[x][y] > 0 and sptSet[y] == False and \
						dist[y] > dist[x] + self.graph[x][y]:
					dist[y] = dist[x] + self.graph[x][y]
					print('dy',dist[y])
				# print('dy2',dist[y])

					# return

		self.printSolution(dist)


# Driver's code
if __name__ == "__main__":
	g = Graph(9)
	g.graph = [
			[0, 4, 0, 0, 0, 0, 0, 8, 0],
			[4, 0, 8, 0, 0, 0, 0, 11, 0],
			[0, 8, 0, 7, 0, 4, 0, 0, 2],
			[0, 0, 7, 0, 9, 14, 0, 0, 0],
			[0, 0, 0, 9, 0, 10, 0, 0, 0],
			[0, 0, 4, 14, 10, 0, 2, 0, 0],
			[0, 0, 0, 0, 0, 2, 0, 1, 6],
			[8, 11, 0, 0, 0, 0, 1, 0, 7],
			[0, 0, 2, 0, 0, 0, 6, 7, 0]
			]

	# g.dijkstra(0)

# This code is contributed by Divyanshu Mehta and Updated by Pranav Singh Sambyal







# Kosaraju's algorithm to find strongly connected components in Python


from collections import defaultdict

class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    # Add edge into the graph
    def add_edge(self, s, d):
        self.graph[s].append(d)

    # dfs
    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        print(d, end='')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

    # transpose the matrix
    def transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # Print stongly connected components
    def print_scc(self):
        stack = []
        visited_vertex = [False] * (self.V)

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False] * (self.V)
        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print("")


g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

# print("Strongly Connected Components:")
# g.print_scc()











# back, forward, cross
import random


class Graph:
	# instance variables
	def __init__(self, v):
		# v is the number of nodes/vertices
		self.time = 0
		self.traversal_array = []
		self.v = v
		# e is the number of edge (randomly chosen between 9 to 45)
		self.e = random.randint(9, 45)
		# adj. list for graph
		self.graph_list = [[] for _ in range(v)]
		# adj. matrix for graph
		self.graph_matrix = [[0 for _ in range(v)] for _ in range(v)]

	# function to create random graph
	def create_random_graph(self):
		# add edges upto e
		for i in range(self.e):
			# choose src and dest of each edge randomly
			src = random.randrange(0, self.v)
			dest = random.randrange(0, self.v)
			# re-choose if src and dest are same or src and dest already has an edge
			while src == dest and self.graph_matrix[src][dest] == 1:
				src = random.randrange(0, self.v)
				dest = random.randrange(0, self.v)
			# add the edge to graph
			self.graph_list[src].append(dest)
			self.graph_matrix[src][dest] = 1

	# function to print adj list
	def print_graph_list(self):
		print("Adjacency List Representation:")
		for i in range(self.v):
			print(i, "-->", *self.graph_list[i])
		print()

	# function to print adj matrix
	def print_graph_matrix(self):
		print("Adjacency Matrix Representation:")
		for i in self.graph_matrix:
			print(i)
		print()

	# function the get number of edges
	def number_of_edges(self):
		return self.e

	# function for dfs
	def dfs(self):
		self.visited = [False]*self.v
		self.start_time = [0]*self.v
		self.end_time = [0]*self.v

		for node in range(self.v):
			if not self.visited[node]:
				self.traverse_dfs(node)
		print()
		print("DFS Traversal: ", self.traversal_array)
		print()

	def traverse_dfs(self, node):
		# mark the node visited
		self.visited[node] = True
		# add the node to traversal
		self.traversal_array.append(node)
		# get the starting time
		self.start_time[node] = self.time
		# increment the time by 1
		self.time += 1
		# traverse through the neighbours
		for neighbour in self.graph_list[node]:
			# if a node is not visited
			if not self.visited[neighbour]:
				# marks the edge as tree edge
				print('Tree Edge:', str(node)+'-->'+str(neighbour))
				# dfs from that node
				self.traverse_dfs(neighbour)
			else:
				# when the parent node is traversed after the neighbour node
				if self.start_time[node] > self.start_time[neighbour] and self.end_time[node] < self.end_time[neighbour]:
					print('Back Edge:', str(node)+'-->'+str(neighbour))
				# when the neighbour node is a descendant but not a part of tree
				elif self.start_time[node] < self.start_time[neighbour] and self.end_time[node] > self.end_time[neighbour]:
					print('Forward Edge:', str(node)+'-->'+str(neighbour))
				# when parent and neighbour node do not have any ancestor and a descendant relationship between them
				elif self.start_time[node] > self.start_time[neighbour] and self.end_time[node] > self.end_time[neighbour]:
					print('Cross Edge:', str(node)+'-->'+str(neighbour))
			self.end_time[node] = self.time
			self.time += 1


# if __name__ == "__main__":
# 	n = 10
# 	g = Graph(n)
# 	g.create_random_graph()
# 	g.print_graph_list()
# 	g.print_graph_matrix()
# 	g.dfs()





