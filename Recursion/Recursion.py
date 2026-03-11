# def DTImplicit(toConsider, avail):

# 	if toConsider == [] or avail == 0:
# 		result = (0, ())
# 	elif toConsider[0][1] > avail:
# 		result = DTImplicit(toConsider[1:], avail)
# 	else:
# 		nextItem = toConsider[0]
# 		withVal, withToTake = DTImplicit(toConsider[1:], avail -nextItem[1])

# 		withVal += nextItem[0]
# 		withoutVal, withoutToTake = DTImplicit(toConsider[1:], avail)
		
# 		if withVal > withoutVal:
# 			result = (withVal, withToTake + (nextItem,))
# 		else:
# 			result = (withoutVal, withoutToTake)
# 	return result

# a = [6,3]
# b = [7,11]
# c = [8,4]
# d = [9,5]
# stuff = [a,b,c,d]

# print(DTImplicit(stuff,10))


# names = [
#     "Adam",
#     [
#         "Bob",
#         [
#             "Chet",
#             "Cat",
#         ],
#         "Barb",
#         "Bert"
#     ],
#     "Alex",
#     [
#         "Bea",
#         "Bill"
#     ],
#     "Ann"
# ]


# def countNames(seq):
# 	cnt = 0
# 	for e in seq:
# 		if not isinstance(e,list):
# 			cnt += 1
# 		else:
# 			cnt += countNames(e)
# 	return cnt

# print(countNames(names))



# def factorial(n):
# 	print(f"factorial() called with n = {n}")
# 	return_value = 1 if n <= 1 else n * factorial(n -1)
# 	print(f"-> factorial({n}) returns {return_value}")
# 	return return_value

# def factorial(n):
# 	print(f"factorial() called with n = {n}")
# 	return_value = 1 if n <= 1 else n * factorial(n -1)
# 	print(f"-> factorial({n}) returns {return_value}")
# 	return return_value

# def count_leaf_items(item_list):
#     """Recursively counts and returns the
#        number of leaf items in a (potentially
#        nested) list.
#     """
#     print(f"List: {item_list}")
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             print("Encountered sublist")
#             count += count_leaf_items(item)
#         else:
#             print(f"Counted leaf item \"{item}\"")
#             count += 1

#     print(f"-> Returning count {count}")
#     return count


# count_leaf_items(names)



# people = ['mel','jane','mario','blessing','Joy']




# assign(people)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers[5::-2])



# def recuradd(mylist):
#     total = 0
#     for i in mylist:
#         if isinstance(i,list):
#             total+=recuradd(i)
#         else:
#             total+=i
#     return total

# lists = [2,4,5,[6,8],9,7,[8,5,[2,3,4],5],6,2]

# print(recuradd(lists))


# def addsum(lst,total):
#     if len(lst)==1:
#         return total+lst[0]
#     else:
#         total+=lst[0]
#         print(total)
#         return addsum(lst[1:],total)

#         # print(total)
#         # return total

# numbers = [1,2,3,4,5,6,7,8,9,10]

# print(addsum(numbers,0)) 








