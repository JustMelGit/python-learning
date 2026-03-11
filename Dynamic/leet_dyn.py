def climbStairs(n):
	if n == 0:
		return 1
	if n < 0:
		return 0
	else:
		return climbStairs(n-1) + climbStairs(n-2)
print(climbStairs(2))

# def climbStairs(n):
# 	memo = [0,1,2]
# 	for i in range(3,n+1):
# 		memo.append((memo[i-1]+memo[i-2]))
# 	return memo[n]


# print(climbStairs(2))

# def tribonacci(n):
# 	memo = [0,1,1]
# 	for i in range(3,n+1):
# 		memo.append((memo[i-3]+memo[i-2]+memo[i-1]))
# 	return memo[n]

# print(tribonacci(4))

# class Solution:
# 	def minCost(self,cost,n,dp):
# 		if dp[n] != 0:
# 			return dp[n]
# 		if n < 0:
# 			return 0
# 		if n == 0 or n == 1:
# 			return cost[n]

# 		dp[n] = cost[n] + min(self.minCost(cost,n-1,dp),self.minCost(cost,n-2,dp))

# 		return dp[n]

# 	def minCostClimbingStairs(self,cost):
# 		n = len(cost)
# 		dp = [0]*n
# 		return min(self.minCost(cost,n-1,dp),self.minCost(cost,n-2,dp))


# c = [10,15,20]
# v = Solution()
# print(v.minCostClimbingStairs(c))


class Solution:
	def robHelper(self,nums,n):
		if n < 0:
			return 0
		return max(nums[n]+self.robHelper(nums,n-2),self.robHelper(nums,n-1))

	def rob(self,nums):
		n = len(nums)-1
		return self.robHelper(nums,n)


# c = [2,2,3,3,3,4]
c = [2,7,9,3,1]
# v = Solution()
# print(v.rob(c))

import collections

class Solution:
    def deleteAndEarn(self, nums):
        cc=collections.Counter(nums)
        print(cc)
        mx=max(cc)
        print(mx)
        comp=[]
        for i in range(mx+1):
            if i in cc:
                comp.append(cc[i]*i)
            else:
                comp.append(0)
        memo=[-1 for _ in range(mx+1)]
        print(comp)
        def dp(i):
            if i<0:
                return 0 
            elif memo[i]>=0:
                return  memo[i]
            else:
                res=max(dp(i-2)+comp[i],dp(i-1))
                memo[i]=res
                return res
        return dp(mx)

# c = [3,4,2]
# c.sort()
# c1 = [2,2,3,3,3,4]
# c1.sort()
# v = Solution()
# print(v.deleteAndEarn(c1))
# print(v.rob(c))



# Python program for the above approach
 
# Function to add edges
def addEdge(adj, u, v):
    adj[u].append(v)
   
# Function to print adjacency list
def adjacencylist(adj, V):
     
    for i in range (0, V):
        print(i, "-> ", end="")
         
        for x in  adj[i]:
            print(x , " ", end="")
       
        print()
     
# Function to initialize the adjacency list
# of the given graph
def initGraph(V, edges, noOfEdges):
 
    adj = [0]* 3
     
    for i in range(0, len(adj)):
        adj[i] = []
   
    # Traverse edges array and make edges
    for i in range(0, noOfEdges) :
 
         # Function call to make an edge
        addEdge(adj, edges[i][0], edges[i][1])
     
 
    # Function Call to print adjacency list
    print(adj)
    adjacencylist(adj, V)
   
# Driver Code
   
# Given vertices
V = 3
 
# Given edges
edges = [[0,1],[1,2],[1,3],[2,3],[3,0]]
 
noOfEdges = 3;
 
# Function Call
# initGraph(V, edges, noOfEdges)
 
# This code is contributed by AR_Gaurav
