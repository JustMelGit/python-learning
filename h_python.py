# def recurP(n):
# 	import string
# 	if n == 1:
# 		return '|.'
# 	else:
# 		return '|.' + '.' + recurP(n-1)

# def floor_pat(n,m):
# 	upper_half = []
# 	half_hgt = int(n/2)
# 	for i in range(1,half_hgt+1):
# 		strg = recurP(i)
# 		left_half = strg[::-1]
# 		line = left_half + strg[1:]
# 		upper_half.append(line)
# 	lower_half = upper_half[len(upper_half)::-1]
	
# 	for e in upper_half:
# 		print(e.center(m,'-'))
	
# 	print('WELCOME'.center(m,'-'))

# 	for e in lower_half:
# 		print(e.center(m,'-'))


# floor_pat(11,33)





# def gradingStudents(grades):
#     # Write your code here
#     for grade in grades:
#         #if its less than or equal to 40 do nothing
#         if grade <38:
#             print(grade)
#         else:
#             # if is not a multiple of 5
#             if not grade%5 == 0:
#                 # check if the difference to the next five multiple is less than 3
#                 if (int(grade/5)+1)*5 - grade < 3:
#                     print((int(grade/5)+1)*5)
#                 else:
#                     print(grade)


# alist = [73,60,38,35]
# gradingStudents(alist)







# def marsExploration(s):
# 	for i in range(0,len(s),3):
# 		print(i)
# 		print(s[i:i+3])

# s = 'SOSSOSSOS'
# s1 = 'SOSSPSSQSSOR'
# # print(marsExploration(s))



# def marsExploration(s):
#     the_sum = 0
#     #test each len(s) with SOS
#     for i in range(0,len(s),3):
#         if not s[i:i+3] == 'SOS':
#             err_str = s[i:i+3]
#             for j in range(len(err_str)):
#                 if err_str[j] != 'SOS'[j]:
#                     the_sum += 1
#     return the_sum




# print(marsExploration(s1))
# from collections import Counter
# import string
# def weightedUniformStrings(s, queries):
#     alpha_dict = {}
#     for i,v in enumerate(string.ascii_lowercase):
#         alpha_dict[v] = i+1
#     vals = []
#     for k,v in Counter(s).items():
#         alp_val = alpha_dict[k]
#         if v == 1:
#             vals.append(alp_val)
#         else:
#             for i in range(1,v+1):
#                 vals.append(alp_val*i)
#     t_val = []
#     for e in queries:
#         if e in vals:
#             t_val.append('Yes')
#         else:
#             t_val.append('No')
#     return alpha_dict,t_val

# q = [6,1,3,12,5,9,10]






# def weightedUniformStrings(s, queries):
# 	alpha_dict = {}
# 	for i,v in enumerate(string.ascii_lowercase):
# 		alpha_dict[v] = i+1
# 	vals = []
# 	for k,v in Counter(s).items():
# 		alp_val = alpha_dict[k]
# 		if v == 1:
# 			vals.append(alp_val)
# 		else:
# 			for i in range(1,v+1):
# 				vals.append(alp_val*i)
# 	return ('Yes' if e in vals else 'No' for e in queries)

# # print(weightedUniformStrings('abccddde',q))





# def weightedUniformStrings(s, queries):
#     alpha_dict = {}
#     for i,v in enumerate(string.ascii_lowercase):
#         alpha_dict[v] = i+1
#     vals = set()
#     vals_l = []
#     cnt = 0
#     past = ''
#     for e in s:
#         if e == past:
#             cnt += 1
#         else:
#             cnt = 1
#             past = e
#         vals.add(alpha_dict[e]*cnt)
#         vals_l.append(alpha_dict[e]*cnt)
#     print(vals)
#     print(vals_l)
#     return ('Yes' if e in vals else 'No' for e in queries)

# print(list(weightedUniformStrings('abccddde',q)))









# def separateNumbers(s):
# 	char = s[0]
# 	f_di = ''
# 	i = 0
# 	while len(s) > 0:
# 		print('s',s)
# 		char_1 = int(char)+1
# 		print('ch',char,'ch1',char_1)
# 		t_str = s[len(char):]
# 		print('ts',t_str)
# 		if t_str.find(str(char_1))==0:
# 			if not f_di: 
# 				f_di = char
# 				print(f_di)
# 			# char = str(char_1+1)
# 			s = s[(s.index(str(char_1))+len(char)):]
# 			char = str(char_1+1)
# 			if char == s or t_str == str(char_1):
# 				return 'YES',f_di

# 		else:
# 			if f_di or len(char)>len(s):
# 				return 'NO'
# 			char = char+s[i+1]
# 			i += 1
# 		print()
# 	# print(i)
# print(separateNumbers('101103'))





# def separateNumbers(s):
# 	f_str = ''
# 	exp_str = ''
# 	char = s[0]
# 	i = 0
# 	while i < len(s):
# 		char_1 = int(char)+1
# 		t_str = s[len(char):]
# 		if t_str.find(str(char_1)) == 0:
# 			if not f_str:
# 				f_str = char
# 				exp_str += f_str
# 				break
# 		else:
# 			try:
# 				char += s[i+1]
# 				if len(char) > len(s)//2:
# 					break
# 			except:
# 				break
# 		i += 1
# 	while len(exp_str) < len(s):
# 		exp_str += str(char_1)
# 		char_1 += 1

# 	if exp_str == s:
# 		print('YES',f_str)
# 	else:
# 		print('NO',f_str)


# lis = [
# '90071992547409929007199254740993',
# '45035996273704964503599627370497',
# '22517998136852482251799813685249',
# '11258999068426241125899906842625',
# '562949953421312562949953421313',
# '90071992547409928007199254740993',
# '45035996273704963503599627370497',
# '22517998136852481251799813685249',
# '11258999068426240125899906842625',
# '562949953421312462949953421313'
# ]
# # for i in range(10):
# # 	separateNumbers(lis[i])



# s = '90071992547409929007199254740993'



# def separateNumbers(s):
# 	f_str = ''
# 	exp_str = ''
# 	char = s[0]
# 	i = 0
# 	while i < len(s):
# 		char_1 = int(char)+1
# 		t_str = s[len(char):]
# 		if t_str.find(str(char_1)) == 0:
# 			if not f_str:
# 				f_str = char
# 				exp_str += f_str
# 				break
# 		else:
# 			try:
# 				char += s[i+1]
# 			except:
# 				break
# 		i += 1
# 	while len(exp_str) < len(s):
# 		exp_str += str(char_1)
# 		char_1 += 1
# 	if exp_str == s:
# 		print('YES',f_str)
# 	else:
# 		print('NO',f_str)



# def separateNumbersbin(s):
# 	print(s)
# 	if len(s) == 1:
# 		return incre(s[0],s[1])
# 	elif len(s)%2 == 0:
# 		left = separateNumbersbin(s[0:len(s)//2])
# 		right = separateNumbersbin(s[len(s)//2:])
# 		return incre(left,right)
# print(separateNumbersbin('1234'))



# lis = [
# '90071992547409929007199254740993',
# '54035996273704964503599627370497',
# '22517998136852482251799813685249',
# '11258999068426241125899906842625',
# '562949953421312562949953421313',
# '90071992547409928007199254740993',
# '45035996273704963503599627370497',
# '22517998136852481251799813685249',
# '11258999068426240125899906842625',
# '562949953421312462949953421313'
# ]
# for i in range(10):
# 	separateNumbers(lis[i])








# def countApplesAndOranges(s, t, a, b, apples, oranges):
# 	print(len(tuple(e for e in apples if s <= e+a <= t)))
# 	print(len(tuple(e+s for e in oranges if s <= e+b <= t)))


# ap = (2,3,-4)
# o = (3,-2,-4)
# s = 7
# t = 10
# a = 4
# b = 12
# countApplesAndOranges(s,t,a,b,ap,o)





# from collections import Counter
# arr = [1,3,3,4,4,4,5,3]

# def migratoryBirds(arr):
# 	counts = Counter(arr)
# 	return min((counts[key],-key) for key in counts)

# print(migratoryBirds(arr))





# def bisMissing(ar,no):
# 	while len(ar) > 2:
# 		mid = int(len(ar)/2)
# 		if len(ar) == 2:
# 			return ar
# 		if ar[mid] > no:
# 			ar = ar[mid:]
# 		else:
# 			ar = ar[:mid+1]
# 	return ar

# # print(bisMissing(ar,75))




# 100 50 40 20 10
#               |
#               i
# 5 25 50 120
# |
# j
    
    
# def twoPointers1(ranked,player):  
# 	i = len(ranked)-1
# 	j = 0
# 	while j < len(player) and i >= 0:
# 		print(j,i)
# 		if player[j] < ranked[i]:
# 			print('pos1',i+2)
# 			j+=1
# 			i-=1
# 		elif player[j] == ranked[i]:
# 			# print('j',j,'i',i,'i+1',i+1)
# 			j += 1
# 			i -= 1
# 		elif player[j] > ranked[i]:
# 			print('pos',i)
# 			# print('pos',len(ranked)-)
# 			i -= 1
# 			# j+=1
# 			# print(i)




# import math

# def twoPointers(ranked,player):

# 	i = len(ranked)-1
# 	j = 0
# 	while j < len(player) and i >= 0:
# 		print(j)
# 		if player[j] < ranked[i]:
# 			if i == len(ranked)-1:
# 				print('pos',i+2)
# 				j += 1
# 			else:
# 				print('pos11',i)
# 		elif player[j] > ranked[i]:
# 			print('posg', i+1)
# 			j += 1
# 	# 	elif player[j] == ranked[i]:
# 	# 		print('i',i)
# 	# 		# print('j',j,'i',i,'i+1',i+1)
# 	# 		j += 1
# 	# 		i -= 1
# 		cnt = 0
# 		while player[j] > ranked[i] and i > 0:
# 			cnt += 1
# 		i += cnt -1





# def twoPointers2(ranked,player):
# 	ranks = []
# 	i = len(ranked)-1
# 	j = 0
# 	while j < len(player) and i >= 0:
# 		while player[j] >= ranked[i]:
# 			i-=1
# 		if player[j] == ranked[i]:
# 			ranks.append(i)
# 		else:
# 			ranks.append(i+1)
# 			j+=1

# r = [math.inf,100,50,40,20,10,-math.inf]
# p = [5,25,50,120]

# r = [math.inf,100,90,80,75,60,-math.inf]
# p = [50,65,77,90,102]
# twoPointers2(r,p)

# print(math.floor(5/2))




# def superReducedString(s):
#     if len(s) == 0:
#         return 'Empty String'
#     pat = r'(a-z)\1'
#     g = re.match(pat,s)
#     if not g:
#         return s
#     else:
#         s = s.replace(s[g.span],'',1)
#         superReducedString(s)
    
    
# import re

# s = 'james'
# while len(s) > 0:
#    pat = r'([a-z])\1'
#    sts = re.findall(pat,s)
#    for e in sts:
#       s = s.replace(e*2,'',1)
# if s:
#    print(s)
# else:
#    print('Empty')


# def superReducedString(s):
#     if len(s) == 0:
#         return 'Empty String'
#     pat = r'([a-z])\1'
#     g = re.findall(pat,s)
#     if not g:
#         return s
#     else:

#         s = re.sub(pat,'',s)
#         # for e in g:
#         #     s = s.replace(e*2,'',1)
#         return superReducedString(s)


# print(superReducedString(s))





# def alternate(s):
#    max_len = 0
#    pat = r'([a-z]+)[a-z]+(?=\1)'
#    s_set = set(s)
#    for e in it.combinations(s_set,2):
#       new_s = s
#       for f in s_set.difference(e):
#          br = False
#          new_s = new_s.replace(f,'')
      
#          for i in range(len(new_s)-2):
#             test_str = new_s[i:i+3]
#             print(test_str)
#             g = re.match(pat,test_str)
#             if not g:
#                print('I broke')
#                br = True
#                # break
#          if not br:
#             if len(new_s)>max_len:
#                max_len = len(new_s)
#                the_s = new_s
#    return max_len 

# from itertools import combinations




# def alternate(s):
#   maxlen = 0
#   for a, b in it.combinations(set(s), 2):
#     alts = ''.join([c for c in s if c in (a,b)])
#     if not (a*2 in alts or b*2 in alts) and len(alts) > maxlen:
#       maxlen = len(alts)
#   return maxlen


# s = 'abaacdabd'
# s1 = 'beabeefeab'
# s2 = 'bdbd'
# # print(alternate(s2))




# def saveThePrisoner(n,m,s):
#     the_range = list(range(1,n+1))
#     pos = the_range.index(s)
#     the_range = the_range[pos:] + the_range[0:pos]
#     print(m%n-1+s)
#     return the_range[m%n-1]

# n = 352926151 
# m = 380324688 
# s = 94730870

# n = 352926151 
# m = 380324688 
# s = 94730870

# n = 962975336 
# m = 972576181 
# s = 396355184




# def permutationEquation(p):
#     p1 = []
#     for i in range(1,len(p)+1):
#         p1.append(p.index(i)+1)
#     return([p.index(e)+1 for e in p1])

# seq = [4,3,5,1,2]
# print(permutationEquation(seq))





# def flatlandSpaceStations(n, c):
#     if len(c) == n:
#         return 0
#     if len(c) == 1:
#         if c[0] != 0 and c[0] != n-1:
#            return max(n-1-c[0],c[0]-0)
#         else:
#             return n-1
#     else:
#         max_diff = None
#         c.sort()
#         for i in range(1,len(c)):
#             e = [c[i-1],c[i]]
#             if max_diff == None:
#                 max_diff = e
#             else:
#                 if e[1]-e[0] > max_diff[1]-max_diff[0]:
#                     max_diff = e
#         return max(c[0]-0,(max_diff[1]-max_diff[0])//2,n-c[-1]-1)

# print(flatlandSpaceStations(20,[1,6,10,11,13]))






# from itertools import combinations_with_replacement,combinations,permutations

# def stones(n,a,b):
#     perm_diff = combinations_with_replacement([a,b],n-1)

#     print(set(sorted([e for e in perm_diff])))

# stones(3,2,3)





# import math

# def encryption(s):
# 	len_s = len(s)
# 	row = math.floor(math.sqrt(len_s))
# 	col = math.ceil(math.sqrt(len_s))
# 	ptr = 0
# 	word_list = []
# 	for i in range(row):
# 		word_list.append(s[ptr:col+ptr])
# 		ptr += col
# 	codes = []
# 	for i in range(col):
# 		st = ''
# 		for j in range(row):
# 			try:
# 				st += word_list[j][i]
# 			except:
# 				continue
# 		codes.append(st)
# 	return ' '.join(codes)

# s = 'feedthedog'
# print(encryption(s))





# def absolute_permutation(n, k):
#     if k != 0 and n % (2 * k) != 0:
#         return [-1]
#     permutation = []
#     used = [False] * (n + 1)
    
#     for i in range(1, n + 1):
#         if not used[i]:
#             if i + k <= n:
#                 permutation.extend([i + k, i])
#                 used[i] = used[i + k] = True
#             else:
#                 permutation.extend([i, i + k])
#                 used[i] = used[i + k] = True
    
#     return permutation


# n = 4
# k = 2
# result = absolute_permutation(n, k)
# print(result)




# def surfaceArea(A):
# 	area = 2*H*W
# 	def check(i,j):
# 		return A[x+i][y+j] if 0<=x+i<H and 0<=y+j<W else 0
# 	xi = [0,0,1,-1]
# 	yi = [1,-1,0,0]

# 	for x in range(H):
# 		for y in range(W):
# 			for i,j in zip(xi,yi):
# 				area += max(0, A[x][y] - check(i,j))
# 				print('a',max(0, A[x][y] - check(i,j)))
# 	return area





# def bomberMan(n,grid):
# 	state_two = [''.join(['O' for _ in range(len(grid[0]))]) for _ in range(len(grid))]
# 	if n == 1:
# 		return grid
# 	if n % 2 == 0:
# 		return state_two
# 	seq = []
# 	for i in range(2):
# 		state_init_one = grid
# 		bomb_pos = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]=='O']
# 		state_three = state_two[:]
# 		for pos in bomb_pos:
# 			xi = [0,0,1,-1]
# 			yi = [1,-1,0,0]
# 			state_three[pos[0]] = state_three[pos[0]][0:pos[1]] + '.' + state_three[pos[0]][pos[1]+1:]
# 			for j,k in zip(xi,yi):
# 				row_pos = pos[0]+j
# 				col_pos = pos[1]+k
# 				if 0<=row_pos<len(grid) and 0<=col_pos<len(grid[0]):
# 					state_three[row_pos] = state_three[row_pos][0:col_pos] + '.' + state_three[row_pos][col_pos+1:]
# 		seq.append(state_three)
# 		grid = state_three
# 	if (n//2 - 1) % 2 == 0:
# 		return seq[0]
# 	else:
# 		return seq[1]
	
# grid =['.......', '...O...', '....O..','.......', 'OO.....', 'OO.....']
# grid1 = ['...','.O.','...']

# grid3 = ['.......',
# '...O.O.',
# '....O..',
# '..O....',
# 'OO...OO',
# 'OO.O...',]
# print(bomberMan(5,grid3),sep='\n')






# def plusMinus(arr):
#     neg,pos,zeros = 0,0,0
#     for e in arr:
#         if e<0:
#             neg+=1
#         elif e>0:
#             pos+=1
#         else:
#             zeros+=1
#     for val in pos,neg,zeros:
#         try:
#         	print(format(val/len(arr),'.6f'))
#         except ZeroDivisionError:
#         	print(format(0,'.6f'))       

# plusMinus([])

# alist = [2,3,4]




# def timeConversion(s):
#     pat = r'(\d+):(\d+):(\d+)(.+)'
#     g = re.match(pat,s)
#     hour_format = g.group(1)
#     time_format = g.group(4)
#     if time_format == 'PM':
#     	if hour_format == '12':
#     		hour_format = '12'
#     	else:
#     		hour_format = str(int(hour_format) + 12)
#     	the_time = hour_format+s[2:-2]
#     	return the_time
#     elif hour_format == '12':
#     	hour_format = '00'
#     	the_time = hour_format+s[2:-2]
#     	return the_time
#     else:
#     	return s[:-2]


# s = '01:05:00AM'

# print(timeConversion(s))





# def findMedian(arr):
# 	print(arr.sort())
# 	the_mid = len(arr)//2 + 1

# 	# return arr[the_mid]

# print(findMedian([2,3,4]))




# def countingSort(arr):
#     val =[]
#     aDic = {}
#     aDic = aDic.fromkeys(range(6),0)
#     for i in arr:
#         aDic[i] = aDic.get(i,0) + 1
#     for k in range(0,6):
#     	val.append(aDic[k])
#     sorted_list = []
#     print(val)

# countingSort([1,3,2,1,2,4])




# def leap_year(year):
# 	if year%4 == 0:
# 		if year%100 == 0:
# 			if year%400 == 0:
# 				return True
# 			else:
# 				return False
# 		else:
# 			return True
# 	return False

# print(leap_year(1992))





# def formingMagicSquare(s):
#     new_s = []
#     for e in s:
#         new_s.extend(e)

#     a = [[8,1,6,3,5,7,4,9,2],[6,1,8,7,5,3,2,9,4], [4,9,2,3,5,7,8,1,6], [2,9,4,7,5,3,6,1,8],\
#         [8,3,4,1,5,9,6,7,2], [4,3,8,9,5,1,2,7,6], [6,7,2,1,5,9,8,3,4],[2,7,6,9,5,1,4,3,8]]
        
#     return min(sum(abs(i-j) for i,j in zip(aa,new_s)) for aa in a)


# s1 = [4, 9, 2, 3, 5, 7, 8, 1, 5]
# s =  [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

# print(formingMagicSquare(s))





# def biggerIsGreater(w):
#     for i in range(len(w)-1,-1,-1):
#     	for j in range(i-1,-1,-1):
#     		if w[i] > w[j]:
#     			s = sorted(w[j:i])
#     			w = w[0:j]+w[i:]+''.join(s)
#     			return w
#     return 'no answer'


# def biggerIsGreater1(w):
# 	print(w)
# 	for i in range(len(w)-1,0,-1):
# 		if w[i]>w[i-1]:
# 			# print('i-1',w[i-1])
# 			s = sorted(w[i-1:])
# 			print(s)
# 			c = ''
# 			for j in s:
# 				if j>w[i-1]:
# 					# print(j,w[i-1])
# 					c = j
# 					s.remove(j)
# 					print(s)
# 					break
# 			rep = ''.join(sorted(s))
# 			b = w[:i-1]+c+rep
# 			return b
# 	return 'no answer'


# wo = 'zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgmww'
# w1 = 'zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgw'
# w2 = 'zyyxwwtrrnmlggfeb'
# w1 = 'abcd'

# print(biggerIsGreater(w2))
# l = [wo,w1,w2]
# for e in l:
# 	biggerIsGreater(e)
# 	print(biggerIsGreater(e))

# print(biggerIsGreater(w1))
# print(biggerIsGreater1(wo))





# def gridSearch(G,P):
# 	potential = False
# 	for i in range(0,len(g[0])):
# 		P_test = p[0]
# 		k = 0
# 		for j in range(len(g)):
# 			ele = G[j][i:i+len(P[0])]
# 			print(ele)
# 			if ele == P_test:
# 				k+=1
# 				if k == len(P):
# 					return 'YES'
# 				P_test = P[k]
# 			else:
# 				if ele == P[0]:
# 					k = 1
# 					P_test = P[k]
# 				else:
# 					k = 0
# 					P_test = p[0]
# 	return 'NO'

# g = [
# '1234567890',  
# '0987654321',  
# '1111111111',  
# '1111111111',  
# '2222222222'] 

# print(g)

# p = ['876543',
#      '111111',
#      '111111',
#      ]
# print(gridSearch(g,p))





# def strangeCounter(t):
# 	ts = 1
# 	ts_v = 3
# 	te = 3
# 	while t > ts and t > te:
# 		ts += ts_v

# 		ts_v*=2
# 		te = te + ts_v
# 	return te-t+1

# print(strangeCounter(8))







# def separateNumbers(s):
# 	if len(s) == 1:
# 		print('NO')
# 		return
# 	char = s[0]
# 	print(char)
# 	for i in range(1,len(s)):
# 		if not s[i:].find(str(int(char)+1)) == 0 or char+s[i:i+5] in s[i:]:
# 			char += s[i]
# 			print(char)
# 			if len(char)==len(s):

# 				print(len(char),'h')
# 				print('NO')
# 				return
# 		else:
# 			break
# 	ori = char
# 	print(ori)
# 	s = s[len(char):] 
# 	while len(s) > 0:
# 		char = str(int(char)+1)
# 		if not s.find(char) == 0:
# 			return 'NO'
# 		s = s[len(char):]
# 	print('YES',ori)
# 	return

# s1 = '78910111213'
# s11 = '99910001001'
# s3 = '1234567891011121314151617181920'

# s = '45035996273704964503599627370497'

# print(separateNumbers(s3))





# def isPalindrome(word):
#     reverse = word[-1::-1]
#     return True if reverse == word else False

# def palindromeIndex(s):
#     if isPalindrome(s):
#         return -1
#     for i in range(len(s)//2):
#         if s[i] != s[len(s)-1-i]:
#             new_s = s[:i]+s[i+1:]
#             if isPalindrome(new_s):
#                 return i
#             else:
#                 return len(s) - i - 1
#     return -1
# s = 'aaa'
# print(palindromeIndex(s))


# checker('abcbna')
# checker('fgnfnidynhxebxxxfmxixhsruldhsaobhlcggchboashdlurshxixmfxxxbexhnydinfngf')
# print(palindromeIndex('fgnfnidynhxebxxxfmxixhsruldhsaobhlcggchboashdlurshxixmfxxxbexhnydinfngf'))







# def anagram(s):
#     if len(s) % 2 != 0:
#         return -1 

#     mid = int(len(s) / 2)
#     freq_list = {}
#     for i in range (0, mid):
#         c = s[i]
#         freq_list[c] = freq_list.get(c, 0) + 1
#     ans = 0
#     for i in range (mid, len(s)):
#         c = s[i]
#         if freq_list.get(c, 0) != 0:
#             freq_list[c] -= 1
#         else:
#             ans += 1
#     return ans




# def makingAnagrams1(s1, s2):
#     ans=0
#     s3=set(s1+s2)
#     for i in s3:
#         ans+=abs(s2.count(i)-s1.count(i))
#     return ans




# def gameOfThrones(s):
# 	from collections import Counter
# 	s_cnt = Counter(s)
# 	char_1 = False
# 	for e in s_cnt.values():
# 		if not e%2 == 0:
# 			if e%2 == 1 and char_1 == False:
# 				char_1 = True
# 			else:
# 				return 'NO'
# 	return 'YES'

# a_str = 'cdefghmnopqrstuvw'
# print(gameOfThrones(a_str))





# def stringConstruction(s):
# 	ans = 0
# 	while len(s)>0:
# 		if s[1:].find(s[0]) != -1:
# 			sub = s[0]
# 			f_ind = s[1:].find(s[0])+1
# 			k = 1
# 			j = f_ind+1
# 			while k < f_ind and j < len(s):
# 				if s[k] == s[j]:
# 					sub += s[k]
# 					k+=1
# 					j+=1
# 			ans+= len(sub)
# 			s = s.replace(sub,'')
# 		else:
# 			ans+=1
# 			s = s.replace(s[0:1],'')
# 	return ans	






# def bigSorting(unsorted):
#     unsorted.sort(key=lambda x:int(x))
#     return unsorted




# def insertionSort1(n,arr):
# 	br = False
# 	val = arr[-1]
# 	for i in range(n-1,0,-1):
# 		if val < arr[i-1]:
# 			arr[i] = arr[i-1]
# 			print(i,arr)
# 		else:
# 			print(i)
# 			arr[i] = val
# 			print(arr)
# 			br = True
# 			break
# 	if not br:
# 		arr = [val]+arr[1:]
# 		print(arr)

# s = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
# print(insertionSort1(10,s))




# def runningTime(arr):
#     cnt = 0
#     for i in range(len(arr)):
#         j = i
#         key = arr[i]
#         while j>0 and key<arr[j-1]:
#             arr[j] = arr[j-1]
#             j-=1
#             cnt += 1
#         arr[j] = key
#         # cnt+=1
#     return cnt

# s = [2,1,3,1,2]
# print(runningTime(s))




# def closestNumbers(arr):
# 	arr.sort()
# 	d = arr[1]-arr[0]
# 	result = [arr[0],arr[1]]
# 	for i in range(1,len(arr)-1):
# 		x,y = arr[i],arr[i+1]
# 		if y - x < d:
# 			d = y-x
# 			result = [x,y]
# 			print('r',result)
# 		elif y - x == d:
# 			result.extend([x,y])
# 	return result



# s1 =  s = list(map(int,'-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 -520 -470'.split(' ')))
# # print(s1)
# s = [5,4,3,2]
# print(closestNumbers(s1))




# def icecreamParlor(m,arr):
# 	for i in range(len(arr)-1):
# 		for j in range(i+1,len(arr)):
# 			if sum([arr[i],arr[j]]) == m:
# 				return sorted([i+1,j+1])

# arr = [1,4,5,3,2]
# print(icecreamParlor(4,arr))






# from collections import Counter
# def missingNumbers(arr,brr):
# 	# print(set(arr))
# 	diff = Counter(brr)-Counter(arr)
# 	return diff.keys()


# ar = '203 204 205 206 207 208 203 204 205 206'.split(' ')
# ar = list(map(int,ar))

# br = '203 204 204 205 206 207 205 208 203 206 205 206 204'.split(' ')
# br = list(map(int,br))

# arr = [7,2,5,3,5,3]
# brr = [7,2,5,4,6,3,5,3]
# print(missingNumbers(arr,brr))





# def balancedSums(arr):
# 	arr_sum = sum(arr)
# 	left = 0
# 	# right = arr_sum-arr[0]
# 	# if left == right:
# 		# return 'YES'
# 	for i in range(len(arr)):
# 		left+=arr[i-1] 
# 		right-=arr[i]
# 		if left == right:
# 			return 'YES'
# 	return 'NO'


# s = [5,6,8,11]
# print(balancedSums(s))





# def marcsCakewalk(calorie):
# 	calorie.sort(reverse=True)
# 	return sum(2**j*c for j,c in enumerate(calorie))

# cals = [1,3,2]
# print(marcsCakewalk(cals))





# def findZigZagSequence(a, n):
# 	a.sort()
# 	mid = n//2
# 	a[mid], a[n-1] = a[n-1], a[mid]
# 	st = mid+1
# 	ed = n - 2
# 	while(st <= ed):
# 		a[st], a[ed] = a[ed], a[st]
# 		st = st + 1
# 		ed = ed - 1
# 	for i in range (n):
# 		if i == n-1:
# 			print(a[i])
# 		else:
# 			print(a[i], end = ' ')
# 	return

# seq = [1,2,3,4,5,6,7]
# se = [2,3,5,1,4]
# n = len(se)
# print(findZigZagSequence(se,n))





# def minion_game(string):
# 	s1 = 0
# 	s2 = 0
# 	for i in range(len(string)):
# 		print(string[i])
# 		if string[i].lower() in 'aeiou':
# 			print(len(string))
# 			s1 += len(string) - i
# 		else:
# 			s2 += len(string) - i

# print(minion_game('BANANA'))




# def merge_the_tools(string, k):
# 	vals = (string[i:k+i] for i in range(0,len(string),k))
# 	s = ''
# 	for e in vals:
# 		for char in e:
# 			if char not in s:
# 				s+=char
# 		print(s)
# 		s = ''
# k = 3
# s = 'AABCAAADA'
# merge_the_tools(s,3)







# x = 100
# n = 3
# import math
# r = round(math.pow(x,1/n))


# def powerSumHelper(X, N,r):
# 	if X == 0:
# 		return 1
# 	if X < 0 or r == 0:
# 		return 0
# 	return powerSumHelper(X-math.pow(r,n),N,r-1)+powerSumHelper(X,N,r-1)

# print(powerSumHelper(x,n,r))







# from collections import deque

# def rotations(seq):
# 	s = []
# 	deq_s = deque(seq)
# 	for i in range(3):
# 		deq_s.rotate(-1)
# 		s.append([e for e in deq_s])
# 	return s




# def larrysArray(A):
# 	if A == sorted(A):
# 		return A

# 	for i in range(len(A)):
# 		if A[i] != i+1:
# 			for j in range(i,len(A)):
# 				if i+1 in A[j:j+3] and len(A[j:j+3])==3:
# 					sub = A[j:j+3]
# 					rot = rotations(sub)
# 					print(i,'- >','r - >',rot)
# 					# return

# 					for e in rot:
# 						if e != sub:
# 							A = A[0:j]+e+A[j+3:]
# 							print(A)
# 							new_arr = larrysArray(A)
# 							if new_arr != None:
# 								return new_arr
# 	return 'NO'

# print(larrysArray([9,6,8,12,3,7,1,11,10,2,5,4]))








# def fibonacciModified(t1,t2,n):
# 	memo = [0,t1,t2]
# 	for i in range(3,n+1):
# 		memo.append((memo[i-2]+(memo[i-2+1])**2))
# 	return memo[n]

# print(fibonacciModified(0,1,5))




# def unboundedKnapsack(k, arr,su,n):
# 	if su > k:
# 		return su - arr[n]
# 	if su == k:
# 		return su
# 	if n < 0:
# 		return su
# 	else:
# 		include = unboundedKnapsack(k,arr,su+arr[n],n)
# 		exclude = unboundedKnapsack(k,arr,su,n-1)
# 		return max(include,exclude)

# k = 9
# arr = [2]
# su = 0
# n = len(arr)
# print(unboundedKnapsack(k,arr,su,n-1))





# def getWays(n,c):
# 	def getWaysI(c, n, v, dp):
# 		if (n == 0):
# 			dp[v][n] = 1
# 			return dp[v][n]
# 		if (v == 0):
# 			return 0
# 			if (dp[v][n] != -1):
# 				return dp[v][n]
# 			if (c[v - 1] <= n):
# 				dp[v][n] = getWaysI(c, n - c[v - 1], v, dp) + getWaysI(c, n, v - 1, dp)
# 				return dp[v][n]
# 			else: 
# 				dp[v][n] = getWaysI(c, n, v - 1, dp)
# 				return dp[v][n]
# 	return getWaysI(c,n,v,memo)

# if __name__ == '__main__':

#     c = [1,2,3]
#     n = 4
#     # Print the number of ways of making change for 'n' units using coins having the values given by 'c'
#     v = len(c)
#     memo = [[-1 for i in range(n+1)] for j in range(v+1)]
#     ways = getWays(n, c)
#     print(ways)




# def beautifulBinaryString(b):
# 	sub = '010'
# 	cnt = 0
# 	i = 0
# 	while i < len(b)-2:
# 		print(b[i:])
# 		if b[i:].startswith(sub):
# 			cnt+=1
# 			i+=3
# 		else:
# 			i+=1
# 	return cnt

# print(beautifulBinaryString('0100101010'))



