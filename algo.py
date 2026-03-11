# def findRoot1(x, power, epsilon):
#     low = 0
#     high = x
#     ans = (high+low)/2.0
#     while abs(ans**power - x) > epsilon:
#         if ans**power < x:
#             low = ans
#         else:
#             high = ans
#         ans = (high+low)/2.0
#     return ans


# def search(L, e):
#     def bSearch(L, e, low, high):
#         if high == low:
#             return L[low] == e
#         mid = low + int((high - low)/2)
#         if L[mid] == e:
#             return True
#         if L[mid] > e:
#             return bSearch(L, e, low, mid - 1)
#         else:
#             return bSearch(L, e, mid + 1, high)
        
#     if len(L) == 0:
#         return False
#     else:
#         return bSearch(L, e, 0, len(L) - 1)

# al = ['joy','gift','pat']

# print(search(al,'pat'))




#Selection sort

# def selSort(L):
#     for i in range(len(L) - 1):
#         minIndx = i
#         minVal= L[i]
#         j = i + 1
#         while j < len(L):
#             if minVal > L[j]:
#             minIndx = j
#             minVal= L[j]
#             j += 1
#         temp = L[i]
#         L[i] = L[minIndx]
#         L[minIndx] = temp



#merge

# def merge(left, right, compare):
#     result = []
#     i,j = 0, 0
#     while i < len(left) and j < len(right):
#         if compare(left[i], right[j]):
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while (i < len(left)):
#         result.append(left[i])
#         i += 1
#     while (j < len(right)):
#         result.append(right[j])
#         j += 1
#     return result



# import operator
# def mergeSort(L, compare = operator.lt):
#     if len(L) < 2:
#         return L[:]
#     else:
#         middle = int(len(L)/2)
#         left = mergeSort(L[:middle], compare)
#         right = mergeSort(L[middle:], compare)
#         return merge(left, right, compare)




#quick sort
# import statistics

# def quicksort(numbers):
#     if len(numbers) <= 1:
#         return numbers
#     else:
#         pivot = statistics.median(
#             [
#                 numbers[0],
#                 numbers[len(numbers) // 2],
#                 numbers[-1]
#             ]
#         )
#         items_less, pivot_items, items_greater = (
#             [n for n in numbers if n < pivot],
#             [n for n in numbers if n == pivot],
#             [n for n in numbers if n > pivot]
#         )

#         return (
#             quicksort(items_less) +
#             pivot_items +
#             quicksort(items_greater)
#         )

# als = [4,2,3,7,8]
# print(quicksort(als))







# def insertion_sort(A):
#   for i in range(len(A)):
#       j = i
#       while j>0 and A[j-1] > A[j]:
#           temp = A[j]
#           A[j] = A[j-1]
#           A[j-1] = temp
#           j -= 1
#   return A

# print(insertion_sort([5,2,4,6,1,3]))




# def insertionSort(seq):
#   for i in range(1,len(seq)):
#       j = i
#       while j > 0 and seq[j] < seq[j-1]:
#           seq[j],seq[j-1] = seq[j-1],seq[j]
#           j-=1
#   return seq

# alist = [1,5,4,3,2,6]
# print(insertionSort(alist))





# def almostSorted(arr):



# alist = [1,5,4,3,2,6]
# alist1 = [4,2,5]
# alist2 = [2,3,5,4]
# alist3 = [3,1,2]
# alist4 = [1,5,4,3,2,6]
# alist5 = [1,2,3,8,5,6,7,4]

# sep = list(map(int,'4104 8529 49984 54956 63034 82534 84473 86411 92941 95929 108831 894947 125082 137123 \
#   137276 142534 149840 154703 174744 180537 207563 221088 223069 231982 249517 252211 255192 260283 261543 \
#   262406 270616 274600 274709 283838 289532 295589 310856 314991 322201 339198 343271 383392 385869 389367 \
#   403468 441925 444543 454300 455366 469896 478627 479055 484516 499114 512738 543943 552836 560153 578730 \
#   579688 591631 594436 606033 613146 621500 627475 631582 643754 658309 666435 667186 671190 674741 685292 \
#   702340 705383 722375 722776 726812 748441 790023 795574 797416 813164 813248 827778 839998 843708 851728 \
#   857147 860454 861956 864994 868755 116375 911042 912634 914500 920825 979477'.split(' ')))
# # print(len(sep))
# print(almostSorted(alist1))





# def insertion(seq):
# 	for i in range(len(seq)):
# 		j = i
# 		while j>0 and seq[j]<seq[j-1]:
# 			seq[j-1],seq[j] = seq[j],seq[j-1]
# 			j -= 1
# 	return seq


# seq = [5,4,7,9,3,8]


# print(insertion(seq))



def calAmount(month,annual,months):
	start = 1
	current = 4600000
	monthly = annual/12/100
	while start<=months:
		ints = monthly*current
		current+=ints+month
		print(start,'----',current,'---',ints)
		start+=1
	return current-450000


# print(calAmount(750000,11,36))

A = [1,2,3]
B = [5,6,7]
C = [8,9,10]

x = [A]+B+C

# print(x)

x = 2
# print(eval('x+3'))

# eval('print(7+3)')


# print(any([]))

# from string import ascii_lowercase

# res = ascii_lowercase

# print(res)


# from collections import Counter
# from string import ascii_lowercase




def fact(n):
	print(f"factorial{n}")
	if n <= 1:
		result = 1
	else:
		result = n* fact(n-1)
	print('returning',result)
	return result

n = 3
print(fact(n))
