# x = ['foo', 'bar', 'baz', 'foo', 'qux']
# mc = [('b', 3), ('a', 2), ('c', 2)]
# y = [5,2,9,7]
# # x.sort(reverse = True)
# z = sorted(mc,key=lambda element:(-element[1],element[0]))




# from collections import Counter
# if __name__=="__main__":
#     cnt = Counter(input())
 
    
#     lstcnt = (sorted(cnt.most_common(), key=lambda element: (-element[1], element[0]) ))
#     [print("{k} {v}".format(k=a, v=b)) for (a, b) in lstcnt[:3]]




# lstcnt = [(1,3),(2,2),(6,3),(5,2)]

# # [print("{v} {k}".format(k=a,v=b)) for (a,b) in lstcnt]

# val = [(a,b) for (a,b) in lstcnt]

# print(val)




# def chk(arr):
# 	return any([e > 0 for e in arr]) and all([e % 10 == e for e in arr])

# print(chk(ar))

# print((all([e > 0 for e in arr]) and any([e % 10 == e for e in arr])))




# def chk(arr):
# 	return any([e > 0 for e in arr]) and all([e % 10 == e for e in arr])

# print(chk(ar))

# print((all([e > 0 for e in arr]) and any([e % 10 == e for e in arr])))





# from fractions import Fraction
# a_frac = Fraction(25,4)

# print(a_frac.numerator,a_frac.denominator)







# print(list(
# 		tuple(
# 			zip(*((x[0],x[1],x[2]) 
# 					for x in aseq)))))
# aseq = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# print(list(zip(*aseq)))



# def better_grouper(inputs, n):
#     iters = [iter(inputs)] * n
#     return zip(*iters)






# ar = [(9,3,2),(9,4,1),(4,3,1),(5,2,1)]

# print(sorted(ar,key=lambda x: (-x[0],x[1])))

# aset = {80,80,70,60,60,50,50,50}
# ar = [80,70,60,50,40,30]







# import re
# # items = [
# # 12,
# # 'insert 0 5',
# # 'insert 1 10',
# # 'insert 0 6',
# # 'print',
# # 'remove 6',
# # 'append 9',
# # 'append 1',
# # 'sort',
# # 'print',
# # 'pop',
# # 'reverse',
# # 'print'
# # ]

# items = [
# 4,
# 'append 1',
# 'append 2',
# 'insert 1 3',
# 'print'
# ]




# items2 = [
# 12,
# 'insert 0 5',
# 'insert 1 10',
# 'insert 0 6',
# 'print',
# 'remove 6',
# 'append 9',
# 'append 1',
# 'sort',
# 'print',
# 'pop',
# 'reverse',
# 'print'
# ]



# alist = []

# for _ in range(1,N):

# 	com_line = input().split(' ')
# 	com = com_line[0]
# 	arg = com_line[1:]

# 	if com != 'print':
# 		eval('alist.{0}{1}'.format(com,tuple(map(int,arg))))
# 	else:
# 		print(alist)








# import fileinput,re

# # Matches fields enclosed in square brackets:
# field_pat = re.compile(r'\[(.+?)\]')
# # We'll collect variables in this:
# scope = {}
# # This is used in re.sub:
# def replacement(match):
# 	code = match.group(1)
# 	try:
# 	# If the field can be evaluated, return it:
# 		return str(eval(code, scope))
# 	except SyntaxError:
# 	# Otherwise, execute the assignment in the same scope...
# 		exec(code,scope)
# 	# ...and return an empty string:
# 	return ''

# print(scope)
# s = 'the sum of 2 + 8 is [2+8] '
# s1 = '[name="Mr. Gumby"]Hello, [name]'
# field_pat = re.compile(r'\[(.+?)\]')

# print(field_pat.sub(replacement,s1))





# a_dict = {}
# import itertools
# records = [['chi',20.0],['beta',50.0],['alpha',50]]
# key_func = lambda x: x[1]
# for key,group in itertools.groupby(records,key_func):
# 	a_dict[key] = sorted([e[0] for e in list(group)])
# print(a_dict)





# from collections import Counter

# myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]

# myCounter = Counter(myList)

# print(myCounter)

# print(myCounter.most_common(4))

# print(sorted(myCounter.most_common(4),key=lambda x:(x[1],-x[0]),reverse=True))






# import operator
# print(operator.lt(3,2))




# arr = [2,4,5]
# for e in ((a,b) for a,b in zip(arr,arr[1:])):
# 	print(e)





# 	sarr = sorted(arr)
# 	ans = [i+1 for i,(a,b) in enumerate(zip(arr,sarr)) if a!=b]
# 	if len(ans) == 0:
# 		print('yes')
# 	elif len(ans) == 2:
# 		print(f"yes\nswap {ans[0]} {ans[1]}")
# 	elif len(ans)>2 and all([arr[i-1]>arr[i] for i in ans[:-1]]):
# 		print(f"yes\nreverse {ans[0]} {ans[-1]}")
# 	else:
# 		print('no')






# import itertools as it

# seq = ['A','B','C']

# from collections import deque

# lst = []
# de_seq = deque(seq)

# for i in range(2):
# 	de_seq.rotate(-1)
# 	lst.append(de_seq)
# 	de_seq.rotate(-1)
# print(lst)


# de_seq.rotate(-1)

# print(de_seq)







# def combo(mat):
# 	combinations = []
# 	col_no = len(mat[0])
# 	row_no = len(mat)
# 	for i in range(row_no):
# 		for j in range(col_no):
# 			items = [mat[i][j]] + mat[(i+1)%row_no][:j] + mat[(i+1)%row_no][j+1:]
# 			combinations.append(items)
# 	combinations += mat
# 	return combinations
# seq = [[1,2,3],[4,5,6]]

# print(combo(seq))