
# def fib(n,memo={}):
# 	if memo.get(n):
# 		return memo[n]
# 	if n == 0:
# 		return 0
# 	if n == 1:
# 		return 1
# 	else:
# 		memo[n] = fib(n-1,memo) + fib(n-2,memo)
# 		# print(memo)
# 		return memo[n]

# print(fib(50))
# print()



# def fibTab(n):
# 	memo = [0,1]
# 	for i in range(2,n+1):
# 		memo.append((memo[i-1]+memo[i-2]))

# 	return memo[n]

# print(fibTab(4))



# def longestIncreasingSub(seq):
# 	arr = [1 for i in range(len(seq))]
# 	for i in range(1,len(seq)):
# 		for j in range(i):
# 			if seq[i] > seq[j] and arr[i] <= arr[j]:
# 				arr[i]+=1
# 	print(arr)

# seq = [5,8,7,1,9]
# print(longestIncreasingSub(seq))



# def minOperationsReduceNumZero(nums,x,left,right,count):
# 	if left == right:
# 		return count+1
# 	if x == 0:
# 		return count
# 	if x < 0 or left > right:
# 		print(x,left,right)
# 		return float('inf')
# 	else:
# 		left_side = minOperationsReduceNumZero(nums,x-nums[left],left+1,right,count+1)
# 		right_side = minOperationsReduceNumZero(nums,x-nums[right],left,right-1,count+1)
# 		return min(left_side,right_side)

# # nums = [1]
# nums = [1,1,4,2,3]
# x = 5
# l = 0
# r = len(nums)-1
# print(minOperationsReduceNumZero(nums,x,l,r,0))



# def LCS(s1,s2,n,m,mem):
# 	if mem[n][m] != None:
# 		return mem[n][m]
# 	if n == 0 or m == 0:
# 		return 0
# 	if s1[n-1] == s2[m-1] and n != m:
# 		mem[n][m] = 1+LCS(s1[:n-1],s2[:m-1],n-1,m-1,mem)
# 		return mem[n][m]
# 	else:
# 		mem[n][m] = max(LCS(s1[:n-1],s2[:m],n-1,m,mem),LCS(s1[:n],s2[:m-1],n,m-1,mem))
# 		return mem[n][m]

# s1 = 'AABEBCDD'
# s2 = 'AABEBCDD'
# n = len(s1)
# m = len(s2)
# mem = [[None for i in range(m+1)] for j in range(n+1)]
# print(LCS(s1,s2,n,m,mem))




# def LCS_tab(s1,s2,n,m):
# 	mem = [[None for i in range(m+1)] for j in range(n+1)]
# 	for i in range(n+1):
# 		mem[i][0] = 0
# 	for i in range(m+1):
# 		mem[0][i] = 0
# 	for i in range(1,n+1):
# 		for j in range(1,m+1):
# 			if s1[i-1] == s2[j-1]:
# 				mem[i][j] = 1 + mem[i-1][j-1]
# 			else:
# 				mem[i][j] = max(mem[i-1][j],mem[i][j-1])
# 	return mem
# lcs_matrix = LCS_tab(s1,s2,n,m)



# def get_lcs(s1,matrix):
# 	sub_str = ''
# 	depth = len(matrix)
# 	width = len(matrix[0])
# 	pos = depth-1,width-1
# 	while pos[0] != 0 and pos[1] != 0:
# 		cur_row = pos
# 		left = pos[0],pos[1]-1
# 		top = pos[0]-1,pos[1]
# 		dia = pos[0]-1,pos[1]-1
# 		if matrix[left[0]][left[1]] == matrix[top[0]][top[1]] and matrix[left[0]][left[1]] == matrix[dia[0]][dia[1]]:
# 			if matrix[left[0]][left[1]] != matrix[pos[0]][pos[1]]:
# 				pos = dia
# 			else:
# 				pos = left
# 		else:
# 			arr = [(left[0],left[1],matrix[left[0]][left[1]]),(top[0],top[1],matrix[top[0]][top[1]]),(dia[0],dia[1],matrix[dia[0]][dia[1]])]
# 			arr.sort(key=lambda x:x[2],reverse=True)
# 			pos = arr[0][0:2]
# 		if cur_row[0]-pos[0] == 1 and cur_row[1]-pos[1] == 1:
# 			sub_str = s1[cur_row[0]-1]+sub_str
# 	return sub_str
# print(get_lcs(s1,lcs_matrix))




# def LcsString(s1,s2,lcs):
# 	p1,p2,p3 = 0,0,0
# 	s = ''
# 	for c in lcs:
# 		while s1[p1] != c:
# 			s += s1[p1]
# 			p1 += 1
# 		while s2[p2] != c:
# 			s += s2[p2]
# 			p2 += 1
# 		s += s1[p1]
# 		p1 += 1
# 		p2 += 1
# 	print(s)

# s1 = 'AGGTAB'
# s2 = 'GXTXAYB'
# l = 'GTAB'
# print(LcsString(s1,s2,l))





# def count(coins, n, tar):
# 	if tar == 0:
# 		return 1
# 	if tar < 0:
# 		return 0
# 	if n <= 0:
# 		return 0
# 	return count(coins, n - 1, tar) + count(coins, n, tar-coins[n-1])

# coins = [1, 2, 3]
# n = len(coins)
# print(count(coins, n, 4))




# def coinchange(a, v, n, dp):
#     if (v == 0):
#         dp[n][v] = 1
#         return dp[n][v]
#     if (n == 0):
#         return 0
#     if (dp[n][v] != -1):
#         return dp[n][v]
#     if (a[n - 1] <= v):
#         dp[n][v] = coinchange(a, v - a[n - 1], n, dp) + coinchange(a, v, n - 1, dp)
#         return dp[n][v]
#     else: 
#         dp[n][v] = coinchange(a, v, n - 1, dp)
#         return dp[n][v]
 
 
# # Driver code
# if __name__ == '__main__':
#     tc = 1
#     while (tc != 0):
#         n = 3
#         v = 4
#         a = [1, 2, 3]
#         dp = [[-1 for i in range(v+1)] for j in range(n+1)]
#         res = coinchange(a, v, n, dp)
#         print(res)
#         tc -= 1



# # Driver program to test above function
# coins = [1, 2, 3]
# n = len(coins)
# print(count(coins, n, 4))

# n = 3
# v = 4
# a = [1, 2, 3]
# memo = [[-1 for i in range(v+1)] for j in range(n+1)]
# print(memo)


# def count(coins, n, sum,memo):

# 	if memo[n][v] != -1:
# 		return memo[n][v]

# 	# If sum is 0 then there is 1
# 	# solution (do not include any coin)
# 	if (sum == 0):
# 		memo[n][v] = 1
# 		return 1

# 	# If sum is less than 0 then no
# 	# solution exists
# 	if (sum < 0):
# 		memo[n][v] = 0
# 		return 0

# 	# If there are no coins and sum
# 	# is greater than 0, then no
# 	# solution exist
# 	if (n <= 0):
# 		memo[n][v] = 0
# 		return 0

# 	# count is sum of solutions (i)
# 	# including coins[n-1] (ii) excluding coins[n-1]
# 	result = count(coins, n - 1, sum,memo) + count(coins, n, sum-coins[n-1],memo)
# 	memo[n][v] = result
# 	print(memo)
# 	return memo[n][v]


# # Driver program to test above function
# coins = [1, 2, 3]
# n = len(coins)
# print(count(coins, n, 4,memo))






# def coin_change_min(coins,amount,n):
# 	if amount == 0:
# 		return 0
# 	if n == 0:
# 		return float('inf')
# 	if coins[n-1] > amount:
# 		return coin_change_min(coins,amount,n-1)
# 	return min(1+coin_change_min(coins,amount-coins[n-1],n),coin_change_min(coins,amount,n-1))

# coins_lst = [1,2,5]
# amt = 11
# n = len(coins_lst)
# # print(coin_change_min(coins_lst,amt,3))


# def coin_change_ways(coins,amount,n):
# 	if amount == 0:
# 		return 1
# 	if n == 0:
# 		return 0
# 	if coins[n-1] > amount:
# 		return coin_change_ways(coins,amount,n-1)
# 	return coin_change_ways(coins,amount-coins[n-1],n)+coin_change_ways(coins,amount,n-1)


# coins_lst = [8,3,1,2]
# amt = 3
# n = len(coins_lst)
# print(coin_change_ways(coins_lst,amt,n))



# mem = [[None for i in range(amt+1)] for j in range(n+1)]

# def coin_change_ways_tab(coins,amount,n,mem):
# 	for i in range(n+1):
# 		mem[i][0] = 1
# 	for i in range(1,amount+1):
# 		mem[0][i] = 0
# 	for i in range(1,n+1):
# 		for j in range(1,amount+1):
# 			if coins[i-1] > j:
# 				mem[i][j] = mem[i-1][j]
# 			else:
# 				mem[i][j] = mem[i][j-coins[i-1]]+mem[i-1][j]
# 	return mem[n][amount]

# print(coin_change_ways_tab(coins_lst,amt,n,mem))





# mem = [[None for i in range(amt+1)] for j in range(n+1)]

# def coin_change_min_tab(coins,amount,n,mem):
# 	for i in range(n+1):
# 		mem[i][0] = 0
# 	for i in range(1,amount+1):
# 		mem[0][i] = float('inf')
# 	for i in range(1,n+1):
# 		for j in range(1,amount+1):
# 			if coins[i-1] > j:
# 				mem[i][j] = mem[i-1][j]
# 			else:
# 				mem[i][j] = min(1+mem[i][j-coins[i-1]],mem[i-1][j])
# 	return mem[n][amount]

# print(coin_change_min_tab(coins_lst,amt,n,mem))


# mem = [[None for i in range(amt+1)] for j in range(n+1)]




# def coin_change_min_tab(coins,amount,n,mem):
# 	for i in range(n+1):
# 		mem[i][0] = 0
# 	for i in range(1,amount+1):
# 		mem[0][i] = float('inf')
# 	for i in range(1,n+1):
# 		for j in range(1,amount+1):
# 			if coins[i-1] > j:
# 				mem[i][j] = mem[i-1][j]
# 			else:
# 				mem[i][j] = min(1+mem[i][j-coins[i-1]],mem[i-1][j])
# 	return mem[n][amount]

# print(coin_change_min_tab(coins_lst,amt,n,mem))







# def knapsack(wt,profit,w,n,memo = {}):
# 	if memo[n][w] != -1:
# 		return memo[w][n]
# 	if n == 0 or w == 0:
# 		return 0
# 	if wt[n] > w:
# 		result = knapsack(wt,profit,w,n-1)
# 		memo[n][w] = result
# 		return result
# 	else:
# 		result = max(knapsack(wt,profit,w,n-1,memo), profit[n]+knapsack(wt,profit,w-wt[n],n-1,memo))
# 		memo[n][w] = result
# 		print(memo)
# 		return result

# wt_arr = [3,2,4]
# pr_arr = [6,8,7]
# no = len(wt_arr)
# we = 8

# memo = [[-1 for i in range(we+1)] for j in range(no+1)]
# print(memo)

# print(knapsack(wt_arr,pr_arr,we,no-1,memo))




# def subsetSum(target,seq,n):
# 	if target == 0:
# 		return True
# 	if n < 0:
# 		return False
# 	else:
# 		return subsetSum(target-seq[n],seq,n-1) or subsetSum(target,seq,n-1)
# print(subsetSum(7,[3,2,4],2))




# def subset_sum(sum_value,alist,n,mem):
# 	if mem[n][sum_value] != None:
# 		return mem[n][sum_value]
# 	if sum_value == 0:
# 		return True
# 	if n < 0 or sum_value < 0:
# 		return False
# 	result = subset_sum(sum_value-alist[n-1],alist,n-1,mem) or subset_sum(sum_value,alist,n-1,mem)
# 	return result

# my_lst = [2,2,3] 
# tar = 10
# n = len(my_lst)

# mem = [[None for i in range(tar+1)] for j in range(n+1)]

# # print(subset_sum(tar,my_lst,n,mem))




# def subsetSum(target,seq,n,memo):
# 	for i in range(no+1):
# 		memo[i][0] = True
# 	for i in range(sums+1):
# 		memo[0][i] = False
# 	for i in range(1,no+1):
# 		for j in range(1,sums+1):
# 			if memo[i][j] == -1:
# 				if j-seq[i-1] < 0:
# 					memo[i][j] = memo[i-1][j]
# 				else:
# 					memo[i][j] = memo[i-1][j] or memo[i-1][j-seq[i-1]]
# 	return memo[no][sums]


# arr = [3,34,4,12,5,2]
# no = 6
# sums = 9
# memo = [[-1 for i in range(sums+1)] for j in range(no+1)]

# print(subsetSum(sums,arr,no,memo))




# def subset_tab(target,alist,n,mem):
# 	for i in range(n+1):
# 		mem[i][0] = True
# 	for i in range(1,target+1):
# 		mem[0][i] = False
# 	# print(mem)
# 	for i in range(1,n+1):
# 		for j in range(1,target+1):
# 			if alist[i-1] > j:
# 				mem[i][j] = mem[i-1][j]
# 			else:
# 				mem[i][j] = mem[i-1][j-alist[i-1]] or mem[i-1][j]
# 	return mem[n][target]

# print(subset_tab(tar,my_lst,n,mem))




# def cutRod(price,index,n):
# 	print(index)
# 	if index == 0:
# 		return n*price[0]

# 	notCut = cutRod(price,index-1,n)
# 	cut = float("-inf")
# 	rod_length = index + 1
# 	# print('i',index)
# 	# print('r',rod_length)
# 	if rod_length <= n:
# 		cut = price[index] + cutRod(price,index,n-rod_length)
# 		# print(cut)
# 	return max(notCut,cut)

# arr = [1,5,8,9]
# size = len(arr)
# print('Maiximum Obtainable Value is ',cutRod(arr,size-1,size))



# def cutRod(price,index,n,dp):
# 	if index == 0:
# 		return n*price[0]
# 	if dp[index][n] != -1:
# 		return dp[index][n]

# 	notCut = cutRod(price,index-1,n,dp)
# 	cut = float('-inf')
# 	rod_lenght = index + 1
# 	if rod_lenght <= n:
# 		cut = price[index] + cutRod(price,index,n-rod_lenght,dp)
# 	dp[index][n] = max(notCut,cut)
# 	return dp[index][n]

# if __name__ == '__main__':
# 	arr = [1,5,8,9,10,17,17,20]
# 	size = len(arr)
# 	dp = []
# 	temp = []
# 	for i in range(0,size+1):
# 		temp.append(-1)
# 	for i in range(0,size):
# 		dp.append(temp)
# 	print(dp)
# 	print('Maximum obtainable Value is :', end = ' ')
# 	print(cutRod(arr,size-1,size,dp))



# def cutRod2(lenght,price):
# 	if lenght == 0:
# 		return 0
# 	maxval = float('-inf')
# 	for i in range(1,lenght+1):
# 		temp = price[i-1] + cutRod2(lenght-i,price)
# 		if temp > maxval:
# 			maxval = temp
# 		print('maxval',maxval)
# 	return maxval

# arr = [1,5,4]
# l = len(arr)
# print(cutRod2(l,arr))



# def rodCutting(lengths,prices,rl,n):
# 	if n == 0 or rl <= 0:
# 		return 0
# 	if length[n-1] > rl:
# 		return rodCutting(lengths,prices,rl,n-1)
# 	else:
# 		return max(prices[n-1]+rodCutting(lengths,prices,rl-length[n-1],n),rodCutting(lengths,prices,rl,n-1))

# length = [1,2,3,4,5,6,7,8]
# price = [1,5,8,9,10,17,17,20]

# print(rodCutting(length,price,8,8))


def Locate(t,k,memo,n):
	if memo[n][k] != float('inf'):
		return memo[n][k]
	if len(t) == 1 and k >= 1:
		memo[n][k] = 0
		return memo[n][k]
	if k == 1:
		memo[n][k] = (t[-1]-t[0])/2
		return memo[n][k]
	
	c = float('inf')
	for x in range(len(t)-1):
		c = min(c,max((t[x]-t[0])/2,Locate(t[x+1:],k-1,memo,n-(x+1))))
		memo[n][k] = c
	print(memo)
	return c

k = 3
to = [1,3,6,7]
n = len(to)
memo = [[float('inf') for j in range(k+1)] for j in range(n+1)]
print(Locate(to,k,memo,n))



# def Locate(t,k):
# 	if len(t) == 1 and k >= 1:
# 		return 0
# 	if k == 1:
# 		return (t[len(t)-1]-t[0])/2
	
# 	c = float('inf')
# 	for x in range(len(t)-1):
# 		print('x',x)
# 		# print('first c = ', c)
# 		a = (t[x]-t[0])/2
# 		# print('a',a,'k',k)
# 		b = Locate(t[x+1:],k-1)
# 		# print('b',b)
# 		c = min(c,max((a,b)))
# 		# print('c',c)
# 		print()
# 	return c

# k = 3
# to = [1,3,6,7]
# n = len(to)
# print(Locate(to,k))




# def Locate(t,k,n,memo):
# 	# print(memo)
# 	if memo[n][k] != float('inf'):
# 		return memo[n][k]

# 	if len(t) == 1 and k >= 1:
# 		return 0
# 	if k == 1:
# 		memo[n][k] = (t[len(t)-1]-t[0])/2
# 		# print(memo)
# 		return memo[n][k]
	
# 	c = float('inf')
# 	for x in range(len(t)-1):
# 		print('x = ',x+1)
# 		a = (t[x]-t[0])/2
# 		b = Locate(t[x+1:],k-1,x+1,memo)
# 		c = min(c,max((a,b)))
# 		memo[x+1][k] = c
# 		print(memo)
# 	return memo[x+1][k]
# 	# return c

# k = 1
# to = [1,3,6,7]
# n = len(to)

# memo = [[float('inf') for i in range(k+1)] for j in range(n+1)]
# # print(memo)

# print(Locate(to,k,n,memo))

# def LocateTab(towns,start,end,k,memo):
# 	for i in range(len(memo)):
# 		memo[i][1] = (towns[end]-towns[i])/2
# 	for i in range(k+1):
# 		memo[end][i] = 0
# 	for j in range(2,k+1):
# 		for i in range(end,-1,-1):
# 			c = float('inf')
# 			for x in range(end-1,-1,-1):
# 				c = min(c,max(abs((towns[x]-towns[i])/2),memo[x+1][j-1]))
# 			memo[i][j] = c
# 	return memo[0][k]

# k = 4
# to = [1,3,6,7]
# n = len(to)
# memo = [[None for j in range(k+1)] for j in range(n)]

# print(LocateTab(to,0,n-1,k,memo))





# def interleave_strings(s1,s2,s3,p1,p2,p3,mem):
# 	print(p1,p2,p3)
# 	key = str(p1)+'*'+str(p2)+'*'+str(p3)
# 	if mem.get(key) != None:
# 		return mem.get(key)
# 	if p1 == len(s1) and p2 == len(s2):
# 		return True
# 	if p1 == len(s1):
# 		return s2[p2] == s3[p3] and interleave_strings(s1,s2,s3,p1,p2+1,p3+1,mem)
# 	if p2 == len(s2):
# 		return s1[p1] == s3[p3] and interleave_strings(s1,s2,s3,p1+1,p2,p3+1,mem)

# 	one = False
# 	two = False
# 	if s1[p1] == s3[p3]:
# 		one = interleave_strings(s1,s2,s3,p1+1,p2,p3+1,mem)
# 	if s2[p2] == s3[p3]:
# 		two = interleave_strings(s1,s2,s3,p1,p2+1,p3+1,mem)
# 	mem[key] = one or two
# 	return mem[key]


# s1 = 'aabcc'
# s2 = 'dbbca'
# s3 = 'aadbbcbcac'
# mem = {}
# print(interleave_strings(s1,s2,s3,0,0,0,mem))







