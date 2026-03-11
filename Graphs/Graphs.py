class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)


class WeightedEdge(Edge):
    def __init__(self, src, dest, Tdist, distS):
        self.src = src
        self.dest = dest
        self.Tdist = Tdist
        self.distS = distS
    def getTotalDistance(self):
        return self.Tdist
    def getOutdoorDistance(self):
        return self.distS
    def __str__(self):
        return str(self.src) +'->'+ str(self.dest) + ' (' + str(self.Tdist) + ', ' + str(self.distS) + ')'


class Digraph(object):
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


class WeightedDigraph(Digraph):
    def addEdge (self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append((dest,edge.getTotalDistance(),edge.getOutdoorDistance()))
    def childrenOf(self,node):
        return [e[0] for e in self.edges[node]]


    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d[0]) +' ' + str(d[1:]) + '\n'
        return res[:-1]


def printPath(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(path[i])
        else:
            result = result + str(path[i]) + '->'
    return result


def DFS(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    print ('Current dfs path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            newPath = DFS(graph,node,end,path,shortest)
            if newPath != None:
                return newPath


def DFSShortest(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    print ('Current dfs path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path)<len(shortest):
                newPath = DFSShortest(graph,node,end,path,shortest)
                if newPath != None:
                        shortest = newPath
    return shortest


# def DFSShortest(graph, start, end, path = [], paths = [],shortest = None):
#     #assumes graph is a Digraph
#     #assumes start and end are nodes in graph
#     path = path + [start]
#     print ('Current dfs path:', printPath(path))
#     if start == end:
#         return path
#     for node in graph.childrenOf(start):
#         if node not in path: #avoid cycles
#             if shortest == None or len(path)<len(shortest):
#                 newPath = DFSShortest(graph,node,end,path,paths,shortest)
#                 if newPath != None:
#                     # paths.append([path])
#                     shortest = newPath
#     return shortest



g = WeightedDigraph()
na = Node('a')
nb = Node('b')
nc = Node('c')
nd = Node('d')
ne = Node('e')
nf = Node('f')
ng = Node('g')

g.addNode(na)
g.addNode(nb)
g.addNode(nc)
g.addNode(nd)
g.addNode(ne)
g.addNode(nf)

e1 = WeightedEdge(na,nb,15,10)
e2 = WeightedEdge(na,nc,14,6)
e3 = WeightedEdge(nb,nc,3,1)
e4 = WeightedEdge(nb,ne,7,4)
e5 = WeightedEdge(nd,ne,11,10)
e6 = WeightedEdge(ne,nf,23,20)
e7 = WeightedEdge(nf,nd,8,5)
e8 = WeightedEdge(nc,ne,9,5)


g.addEdge(e1)
g.addEdge(e2)
g.addEdge(e3)
g.addEdge(e4)
g.addEdge(e5)
g.addEdge(e6)
g.addEdge(e7)
g.addEdge(e8)

DFSShortest(g,na,ne)
# print(g)




# def Per(aStr):
#     if len(aStr)==1:
#         yield (aStr[0])
#     else:
#         for l in range(len(aStr)):
#             for n in Per(aStr[:l] + aStr[l+1:]):
#                 yield aStr[l] + n


# def Pairs(aStr):
#     if len(aStr)==2:
#         return [aStr[0:2][::-1]]
#     else:
#         return [aStr[0:2][::-1]] + Pairs(aStr[1:])


# def createEdges(aStr):
#     edge_dict = {}
#     for node in list(Per(aStr)):
#         txt = ''
#         pairs = Pairs(node)
#         edge_dict[node] = []
#         for e in pairs:
#             pos = node.find(e[::-1])
#             if pos == 0:
#                 txt = e + node[len(e):]
#             elif pos == len(node)-len(e):
#                 txt = node[0:pos] + e
#             else:
#                 txt = node[0:pos] + e + node[pos+2:]
#             edge_dict[node].append(txt)
#     return edge_dict

# CreateEdges = createEdges('ABC')

# nodes = []
# nodes.append(Node("ABC")) # nodes[0]
# nodes.append(Node("ACB")) # nodes[1]
# nodes.append(Node("BAC")) # nodes[2]
# nodes.append(Node("BCA")) # nodes[3]
# nodes.append(Node("CAB")) # nodes[4]
# nodes.append(Node("CBA")) # nodes[5]

# g = Graph()
# for n in nodes:
#     g.addNode(n)



# for source_node in nodes:
#     edges = CreateEdges[source_node.getName()]
#     EdgesSet = set()

#     for e in nodes:
#         if e.getName() in edges:
#             EdgesSet.add(Edge(source_node,e))
    
#     for i in EdgesSet:
#         g.addEdge(i)



# def pathLengths(g,nodes,goal):
#     dicLen = {}
#     for e in nodes:
#         dicLen[e.getName()+'->'+goal.getName()] = len(DFSShortest(g,e,goal))
#     return dicLen

# print(pathLengths(g,nodes,nodes[0]))



# edges = [
# Edge(nodes[0],nodes[2]),
# Edge(nodes[0],nodes[1]),
# Edge(nodes[2],nodes[3]),
# Edge(nodes[3],nodes[5]),
# Edge(nodes[5],nodes[4]),
# Edge(nodes[4],nodes[1])
# ]

# for edge in edges:
#     g.addEdge(edge)














































































































































#     nodeNames = list(per('ABC'))
#     nodes = []
#     for name in nodeNames:
#         nodes.append(Node(name))
#     g = Graph()
#     for n in nodes:
#         g.addNode(n)



#         for i in nodes:
#             if i.getName == e:
#                 g.addEdge(Edge(nodes[0],i))

# print(edges('ABC'))

# # Python program to print all paths from a source to destination.


























































# from collections import defaultdict



# # This class represents a directed graph
# # using adjacency list representation
# class Graph:

#     def __init__(self, vertices):
#         # No. of vertices
#         self.V = vertices
        
#         # default dictionary to store graph
#         self.graph = defaultdict(list)

#     # function to add an edge to graph
#     def addEdge(self, u, v):
#         self.graph[u].append(v)

#     '''A recursive function to print all paths from 'u' to 'd'.
#     visited[] keeps track of vertices in current path.
#     path[] stores actual vertices and path_index is current
#     index in path[]'''
#     def printAllPathsUtil(self, u, d, visited, path):

#         # Mark the current node as visited and store in path
#         visited[u]= True
#         path.append(u)

#         # If current vertex is same as destination, then print
#         # current path[]
#         if u == d:
#             print (path)
#         else:
#             # If current vertex is not destination
#             # Recur for all the vertices adjacent to this vertex
#             for i in self.graph[u]:
#                 if visited[i]== False:
#                     self.printAllPathsUtil(i, d, visited, path)
                    
#         # Remove current vertex from path[] and mark it as unvisited
#         path.pop()
#         visited[u]= False


#     # Prints all paths from 's' to 'd'
#     def printAllPaths(self, s, d):

#         # Mark all the vertices as not visited
#         visited =[False]*(self.V)

#         # Create an array to store paths
#         path = []

#         # Call the recursive helper function to print all paths
#         self.printAllPathsUtil(s, d, visited, path)



# # Create a graph given in the above diagram
# g = Graph(4)
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(0, 3)
# g.addEdge(2, 0)
# g.addEdge(2, 1)
# g.addEdge(1, 3)

# s = 2 ; d = 3
# print ("Following are all different paths from % d to % d :" %(s, d))
# g.printAllPaths(s, d)
# # This code is contributed by Neelam Yadav
