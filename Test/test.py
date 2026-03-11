# def retTup(L):
# 	if len(L)==2:
# 		return [L[0:2]]
# 	else:

# 		return [L[0:2]] + retTup(L[1:])

# lis = [6,2,3,4,5,6,8,9]

# print(retTup(lis))
# inside = True
# Last = True

# import re
# if Last and inside and (re.match((r'[^Bible Reading].+\. \(\d+\)'),'common in your territory. (1)')):
# 	print('Yes')
# file =open(r'C:\Users\gnl999935\Documents\March to April.txt','r',encoding='utf-8')
# text = ''

# for e in file:
# 	text+=e.strip()+' '
# # print(text)

# import re

# br = r'Bible Reading: \(\d min\.\) .+? \(\d+?\)'
# rv = r'Return Visit: \(\d min\.\) .+? \(\d+?\)'
# pats = (rv,br)


# # parts = re.findall(Br,text)

# for pat in pats:
# 	parts = re.findall(pat,text)



# for e in parts:
# 	print(e)
# 	print()


# Python3 program for Naive Pattern
# Searching algorithm
# def search(pat, txt):
# 	M = len(pat)
# 	N = len(txt)

# 	# A loop to slide pat[] one by one */
# 	for i in range(N - M + 1):
# 		j = 0
		
# 		# For current index i, check
# 		# for pattern match */
# 		while(j < M):
# 			if (txt[i + j] != pat[j]):
# 				break
# 			j += 1

# 		if (j == M):
# 			print("Pattern found at index ", i)

# # Driver Code
# if __name__ == '__main__':
# 	txt = "AABAACAADAABAAABAA"
# 	pat = "AABA"
# 	search(pat, txt)


# num = [5,8,9,4,5,6,7,8,5,6,1,2,4,8]

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

# print(quicksort([1,3,2]))


# a = [1, 2, 3, 4, 0]
# b = [3, 0, 2, 4, 1]
# c = [3, 2, 4, 1, 5]

# def foo(L):
#     val = L[0]
#     while (True):
#         val = L[val]

# print(foo(b))

# num = 2
# L1 = [5, 0, 2, 4, 6, 3, 1]

# val = 0
# for i in range(0, num):
# 	# print(i)
# 	# print(L)
# 	print(val)
# 	val = L[L[val]]

# # print(val)

# def search(L, e):
#     for i in range(len(L)):
#         if L[i] == e:
#             return True
#         if L[i] > e:
#             return False
#     return False

# print(search(L1,2))


# def search1(L, e):
#     for i in L:
#         if i == e:
#             return True
#         if i > e:
#             return False
#     return False


# print(search1(L1,2))

# def search3(L, e):
#     if L[0] == e:
#         return True
#     elif L[0] > e:
#         return False
#     else:
#         return search3(L[1:], e)

# L = []

# print(search3(L,9))

# x = (1, 2, (3, 'John', 4), 'Hi')

# print(type(x[0]))
# x = range(10, 3, -1)
# for e in x:
	# print(e)
# print(x)
# print(type(range(3)))

# def fiveTimes(e):
# 	return 5*e


# def applyToEach(L, f):

#     for i in range(len(L)):
#         L[i] = f(L[i])

#     print(L)


# testList = [1, -4, 8, -9]

# applyToEach(testList,fiveTimes)


# def applyEachTo(L, x):
#     result = []
#     for i in range(len(L)):
#         result.append(L[i](x))
#     return result

# def square(a):
#     return a*a

# def halve(a):
#     return a/2

# def inc(a):
#     return a+1

# # print(applyEachTo([inc, square, halve, abs], -3))
# print(applyEachTo([inc, square, halve, abs], 3.0))

# animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

# animals['d'] = 'donkey'


# animals['a'] = 'anteater'
# print(animals.keys())
# del animals['b']
# print(len(animals))

# print(animals.values())

# animals = { 'a': ['aardvark','cat','rat','poke'], 'b': ['baboon','aardvark','cat','rat','poke'], \
# 'c': ['coati','baboon','aardvark','cat','rat','poke','baboon','aardvark','cat','rat','poke']}

# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')

# def howMany(aDict):
# 	mydict = {}
# 	keysVal = []
# 	for k,v in aDict.items():
# 		cnt = 0
# 		mydict[k] = None
# 		for e in v:
# 			cnt+=1
# 		mydict[k]=cnt
# 	keysVal = mydict.values()
# 	maxval = max(keysVal)
# 	for k,v in mydict.items():
# 		if v==maxval:
# 			return (k)

# print(howMany(animals))

# def maxOfThree(a,b,c) :
#     """
#     a, b, and c are numbers

#     returns: the maximum of a, b, and c        
#     """
#     if a > b:
#         bigger = a

#     else:
#         bigger = b

#     if c > bigger:
#         bigger = c

#     return bigger

# print(maxOfThree(0, 0, 0))


# def union(set1, set2):
#    """
#    set1 and set2 are collections of objects, each of which might be empty.
#    Each set has no duplicates within itself, but there may be objects that
#    are in both sets. Objects are assumed to be of the same type.

#    This function returns one set containing all elements from
#    both input sets, but with no duplicates.
#    """
#    if len(set1) == 0:
#       return set2
#    elif set1[0] in set2:
#       return union(set1[1:], set2)
#    else:
#       return set1[0] + union(set1[1:], set2)

# print(union('','abc'))

# def rem(x, a):
#     """
#     x: a non-negative integer argument
#     a: a positive integer argument

#     returns: integer, the remainder when x is divided by a.
#     """
#     if x == a:
#         return 0
#     elif x < a:
#         return x
#     else:
#         return rem(x-a, a)

# print(rem(7,5))


# def f(n):
#    """
#    n: integer, n >= 0.
#    """
#    if n <= 1:
#       return n
#    else:
#       return n * f(n-1)

# print(int('1') / 2.0)

# mylist = [10, 20, 30]
# print(mylist.index(11))

# class Clock(object):
# 	def __init__(self, time):
# 		self.time = time
# 	def print_time(self):
# 		time = '6:30'
# 		print(self.time)

# clock = Clock('5:30')
# clock.print_time()

# class Clock(object):
#     def __init__(self, time):
#     	self.time = time
#     def print_time(self, time):
#     	print(time)

# clock = Clock('5:30')
# clock.print_time('10:30')

# class Clock(object):
#     def __init__(self, time):
#     	self.time = time
#     def print_time(self):
#     	print (self.time)

# boston_clock = Clock('5:30')
# paris_clock = boston_clock
# paris_clock.time = '10:30'
# boston_clock.print_time()

# class Weird(object):
#     def __init__(self, x, y): 
#         self.y = y
#         self.x = x
#     def getX(self):
#         return x 
#     def getY(self):
#         return y

# class Wild(object):
#     def __init__(self, x, y): 
#         self.y = y
#         self.x = x
#     def getX(self):
#         return self.x 
#     def getY(self):
#         return self.y

# X = 7
# Y = 8

# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def __repr__(self):
#         return f'Person("{self.first_name}","{self.last_name}",{self})'

# person = Person('John', 'Doe', 25)
# print(repr(person))



# class Coordinate(object):
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def getX(self):
#         # Getter method for a Coordinate object's x coordinate.
#         # Getter methods are better practice than just accessing an attribute directly
#         return self.x

#     def getY(self):
#         # Getter method for a Coordinate object's y coordinate
#         return self.y

#     def __eq__(self,other):
#         return self.x==other.x and self.y==other.y
    
#     def __repr__(self):
#         return f'Coordinate("{self.x}","{self.y}")'


#     def __str__(self):
#         return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'


# c=Coordinate(6,5)
# d = Coordinate(6,5)

# class intSet(object):
#     """An intSet is a set of integers
#     The value is represented by a list of ints, self.vals.
#     Each int in the set occurs in self.vals exactly once."""

#     def __init__(self):
#         """Create an empty set of integers"""
#         self.vals = []
#         self.inter = []

#     def insert(self, e):
#         """Assumes e is an integer and inserts e into self""" 
#         if not e in self.vals:
#             self.vals.append(e)
#         else:
#         	self.inter.append(e)

#     def member(self, e):
#         """Assumes e is an integer
#            Returns True if e is in self, and False otherwise"""
#         return e in self.vals

#     def remove(self, e):
#         """Assumes e is an integer and removes e from self
#            Raises ValueError if e is not in self"""
#         try:
#             self.vals.remove(e)
#         except:
#             raise ValueError(str(e) + ' not found')

#     def intersect(self):
#     	return self.inter

#     def __len__(self):
#     	return len(self.vals)+len(self.inter)


#     def __str__(self):
#         """Returns a string representation of self"""
#         self.vals.sort()
#         return '{' + ','.join([str(e) for e in self.vals]) + '}'


# class Spell(object):
#     def __init__(self, incantation, name):
#         self.name = name
#         self.incantation = incantation

#     def __str__(self):
#         return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
#     def getDescription(self):
#         return 'No description'
    
#     def execute(self):
#         print (self.incantation)  
 

# class Accio(Spell):
#     def __init__(self):
#         Spell.__init__(self, 'Accio', 'Summoning Charm')

# class Confundo(Spell):
#     def __init__(self):
#         Spell.__init__(self, 'Confundo', 'Confundus Charm')

#     def getDescription(self):
#         return 'Causes the victim to become confused and befuddled.'




# def studySpell(spell):
#     print (spell)

# spell = Accio()
# spell.execute()
# studySpell(spell)
# studySpell(Confundo())







# def genSub(lst):
# 	res = []
# 	if len(lst)==0:
# 		return [[]]
# 	smaller = genSub(lst[:-1])
# 	extra = lst[-1:]
# 	new = []
# 	for small in smaller:
# 		new.append(small+extra)
# 	res+=new+smaller
# 	return res

# print([e for e in genSub([3,2,1]) if len(e)==2])






# def selSort(mylist):
# 	for i in range(len(mylist)-1):
# 		minVal = mylist[i]
# 		minIndx = i
# 		j=i+1
# 		while j<len(mylist):
# 			if mylist[j]<minVal:
# 				minVal=mylist[j]
# 				minIndx=j
# 			j+=1
# 		temp = mylist[i]
# 		mylist[i]=mylist[minIndx]
# 		mylist[minIndx]=temp
# 	return mylist


# lst = [2,3,2,5,6,2,4,7,8]
# # print(selSort(lst))
# import operator







# def merge(left, right, compare):
# 	result = []
# 	i,j = 0, 0
# 	while i < len(left) and j < len(right):
# 		if compare(left[i], right[j]):
# 			result.append(left[i])
# 			i += 1
# 		else:
# 			result.append(right[j])
# 			j += 1
# 	while (i < len(left)):
# 		result.append(left[i])
# 		i += 1
# 	while (j < len(right)):
# 		result.append(right[j])
# 		j += 1
# 	return result

# def mergeSort(L,compare=operator.lt):
# 	if len(L)<2:
# 		return L[:]
# 	else:
# 		middle = int(len(L)/2)
# 		left = mergeSort(L[:middle],compare)
# 		right = mergeSort(L[middle:],compare)
# 		return merge(left,right,compare)

# print(mergeSort(lst))






# def biSection(low = 0,high = 100):
# 	low = 0
# 	high = 100
# 	print('Please think of a number between 0 and 100!')
# 	while True:
# 		mid = int((low+high)/2)
# 		print('Is your secret number ' + str(mid) + '?')
# 		userinput = input(f"Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guess correctly.")
# 		if userinput == 'h':
# 			low = low
# 			high = mid
# 			mid = (low+high)/2
# 		elif userinput == 'l':
# 			low = mid
# 			high = high
# 			mid = (low+high)/2
# 		elif userinput=='c':
# 			print(f'Game over. Your secret number was: {mid}')
# 			break
# 		else:
# 			print('Sorry, I did not understand your input.')


# biSection()


# low = 0
# high = 100
# print('Please think of a number between 0 and 100!')
# while True:
# 	mid = int((low+high)/2)
# 	print('Is your secret number ' + str(mid) + '?')
# 	userinput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guess correctly.")
# 	if userinput == 'h':
# 		low = low
# 		high = mid
# 		mid = (low+high)/2
# 	elif userinput == 'l':
# 		low = mid
# 		high = high
# 		mid = (low+high)/2
# 	elif userinput=='c':
# 		print('Game over. Your secret number was: ' + str(mid))
# 		break
# 	else:
# 		print('Sorry, I did not understand your input.')








# def countVowels(s):
# 	count = 0
# 	vowels = ['a','e','i','o','u']
# 	for e in aStr:
# 		if e in vowels:
# 			count+=1
# 	return count

# print(countVowels('James'))


# s = 'kovesmxasav'

# count = 0
# vowels = ['a','e','i','o','u']
# for e in s:
# 	if e in vowels:
# 		count+=1
# print(count)





# def countPat(aStr,pat):
# 	
# cunt = 0

# 	i = len(aStr)
# 	j = len(pat)

# 	for e in range(i-j+1):
# 		j = 0
# 		Flag = False
# 		while j<len(pat):
# 			if not aStr[e+j] == pat[j]:
# 				Flag = True
# 				break
# 			j+=1
# 		if not Flag:
# 			cunt+=1
# 	return cunt
# s = 'azcbobobegghaklbobob'
# print(countPat(s,'bob'))

"""
walk through the len of the string

"""

# cnt = 0
# s = 'obob'
# for i in range(len(s)):
# 	if s[i:i+3] == 'bob':
# 		cnt+=1
# print(cnt)

# s = 'zyxwvutsrqponmlkjihgfedcba'
# txt = s[0]
# longest = s[0]
# i = 1
# while i < len(s):
# 	if s[i] >= s[i-1]:
# 		txt += s[i]
# 	else:
# 		txt = s[i]
# 	i+=1
# 	if len(txt) > len(longest):
# 		longest = txt
# print(longest)

# num = 0
# while num <= 5:
#     print(num)
#     num += 1

# print("Outside of loop")
# print(num)

# no = 2
# while True:
#     if no > 10:
#         break
#     print(no)
#     no+=2
# print('Goodbye!')


# for i in range(2,11,2):
#     print(i)
# print('Goodbye!')


# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 


# s = 'azcbobobegghakl'

# print('b'>'a')





# def longestSubstring(aStr):
# 	sub = ''
# 	listSub = []
# 	for i in range(len(aStr)):
# 		if not sub:
# 			sub+=aStr[i]
# 		elif aStr[i]>sub[-1]:
# 			sub+=aStr[i]

# 		elif (aStr[i]<sub[-1]):
# 			listSub.append(sub)

# 			sub = ''
# 			sub+=aStr[i]
# 	if i == len(aStr)-1 and sub:
# 		listSub.append(sub)

# 	return listSub

# s = 'azcbobobegghakl'
# print(longestSubstring(s))



# def longestSubstring(aStr):
# 	sub = ''
# 	best = ''
# 	for i in range(len(aStr)):
# 		if not sub:
# 			sub+=aStr[i]
# 		elif aStr[i]>sub[-1]:
# 			sub+=aStr[i]
# 		elif (aStr[i]<sub[-1]):
# 			if not best:
# 				best=sub
# 			else:
# 				if len(sub)>len(best):
# 					best=sub
# 			sub = ''
# 			sub+=aStr[i]
# 	if i == len(aStr)-1 and sub and len(sub)>len(best):
# 		best=sub

# 	return best

# s1 = 'azcbobobegghaklbegghh'
# s = 'azcbobobegghakl'
# # print(longestSubstring(s1))




# balance = 484
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

# monthlyInterestRate = annualInterestRate/12.0
# for i in range(0,12):
# 	minimumMonthlyPayment = monthlyPaymentRate * balance
# 	monthlyUnpaidBalance = balance-minimumMonthlyPayment
# 	updatedBalance = monthlyUnpaidBalance+monthlyInterestRate*monthlyUnpaidBalance
# 	balance = updatedBalance
# print('Remaining balance: ' + str(round(balance,2)))
		

		


# def payOneYear(previousBalance,aI):
# 	fPay = 10
# 	mI = aI/12
# 	originalBal = previousBalance
# 	while True:
# 		for i in range(0,12):
# 			monthlyUnpaidBalance = previousBalance - fPay
# 			updatedBalanceEachMonth = monthlyUnpaidBalance + mI*monthlyUnpaidBalance
# 			previousBalance = updatedBalanceEachMonth
# 		if previousBalance<0:
# 			print(fPay)
# 			break
# 		fPay=fPay+10
# 		previousBalance=originalBal
# payOneYear(3926,0.2)


# def payOneYear(previousBalance,aI):

# balance = 3926
# annualInterestRate = 0.2

# fPay = 10
# mI = annualInterestRate/12
# originalBal = balance
# while True:
# 	balance = originalBal
# 	for i in range(0,12):
# 		monthlyUnpaidBalance = balance - fPay
# 		updatedBalanceEachMonth = monthlyUnpaidBalance + mI*monthlyUnpaidBalance
# 		balance = updatedBalanceEachMonth
# 	print(balance)	
# 	if balance<0:
# 		print('Lowest Payment: ' + str(fPay))
# 		break
# 	fPay=fPay+10
	# balance=originalBal


# payOneYear(3926,0.2)



# def payOneYearBis(previousBalance,aI):
# 	mI = aI/12
# 	originalBal = previousBalance
# 	fPayL = previousBalance/12
# 	fPayU = (previousBalance*(1+mI)**12)/12.0
# 	fPay = (fPayL+fPayU)/2
# 	while True:
# 		previousBalance=originalBal
# 		for i in range(0,12):
# 			monthlyUnpaidBalance = previousBalance - fPay
# 			updatedBalanceEachMonth = monthlyUnpaidBalance + mI*monthlyUnpaidBalance
# 			previousBalance = updatedBalanceEachMonth
			
# 		if previousBalance < 0:
# 			if abs(previousBalance) > 0.01:
# 				fPayU = fPay
# 				fPay = (fPay + fPayL)/2
# 			else:
# 				print('Lowest Payment:', round(fPay,2))
# 				break
# 		else:
# 			if previousBalance > 0.01:
# 				fPayL = fPay
# 				fPay = (fPayU + fPay)/2
# 			else:
# 				print('Lowest Payment:', round(fPay,2))
# 				break
	
# payOneYearBis(999999,0.18)



# def payOneYearBis(previousBalance,aI):
# annualInterestRate = 0.18
# balance = 999999


# mI = annualInterestRate/12
# originalBal = balance
# fPayL = balance/12
# fPayU = (balance*(1+mI)**12)/12.0
# fPay = (fPayL+fPayU)/2
# while True:
# 	balance=originalBal
# 	for i in range(0,12):
# 		monthlyUnpaidBalance = balance - fPay
# 		updatedBalanceEachMonth = monthlyUnpaidBalance + mI*monthlyUnpaidBalance
# 		balance = updatedBalanceEachMonth
		
# 	if balance < 0:
# 		if abs(balance) > 0.01:
# 			fPayU = fPay
# 			fPay = (fPay + fPayL)/2
# 		else:
# 			print('Lowest Payment:', round(fPay,2))
# 			break
# 	else:
# 		if balance > 0.01:
# 			fPayL = fPay
# 			fPay = (fPayU + fPay)/2
# 		else:
# 			print('Lowest Payment:', round(fPay,2))
# 			break

	













# def f(x):
# 	import math
# 	return 10*math.e**(math.log(0.5)/5.27 * x)


# def recRad(start,stop,step):
# 	factor = f(start)
# 	if start==stop:
# 		return 0
# 	else:
# 		return factor*step + recRad(start+1,stop,step)

# print(recRad(40,100,1.5))






# def sumNum(aNum):
# 	if aNum//10==0:
# 		return aNum
# 	else:
# 		return aNum%10 + sumNum(aNum//10)
# print(sumNum(6545))






# # import random
# alpha = ['a','p','l','s']

# # pick = random.choice(alpha)

# # print(pick)



# def isWordGuessed(secretWord, lettersGuessed):
# 	i = 0
# 	while i < len(secretWord):
# 		if not secretWord[i] in lettersGuessed:
# 			return False
# 		else:
# 			i+=1
# 	return True

# secretWord = 'apple'

# print(isWordGuessed(secretWord,alpha))









# lettersGuessed = ['e','i','k','p','r','s']

# lettersGuessed1 = []


# def isWordGuessedRecur(secretWord,lettersGuessed):
# 	if secretWord[0] in lettersGuessed:
# 		res = secretWord[0]
# 	else:
# 		res =  '_ '
# 	if len(secretWord)==1:
# 		return (res)
# 	else:
# 		return res + isWordGuessedRecur(secretWord[1:],lettersGuessed)

# secretWord = 'apple'

# print(isWordGuessedRecur(secretWord,lettersGuessed1))

# print(isWordGuessed(secretWord,lettersGuessed))



# def isWordGuessedRecur(secretWord,lettersGuessed):
# 	if len(secretWord)==1:
# 		return secretWord[0] in lettersGuessed
# 	else:
# 		return secretWord[0] in lettersGuessed and isWordGuessedRecur(secretWord[1:],lettersGuessed)

# print(isWordGuessedRecur(secretWord,lettersGuessed))




# def getAvailableLetters(lettersGuessed):
# 	import string
# 	alpha = string.ascii_lowercase
# 	notGuessed = [e for e in alpha if e not in lettersGuessed]
# 	return notGuessed


# letters = ['e', 'i', 'k', 'p', 'r', 's']

# print(getAvailableLetters(letters))

# x = input('Give a name')




# def userDict(no):
# 	Dict = {}
# 	n = 0
# 	import re
# 	pat = r'([a-zA-Z]+)\:([\d]+)'
# 	while True:
# 		try:
# 			userInput = input('Give a name and mark separated by commas (e.g Jane:80): ')
# 			matchItem = re.match(pat,userInput)
# 			name,mark = matchItem.group(1),matchItem.group(2)
# 			Dict[name] = mark
# 			n+=1
# 			if n==no:
# 				print('Your dictionary was ')
# 				print(Dict)
# 				break
# 		except:
# 			print('not a valid input')

# userDict(2)

# txt = "I like bananas"

# x = txt.replace("bananas", "apples")

# print(x)

# s = 'ABCD'

# print(s.index('AB'))
# import re
# regex = r'(\w+),\1'
# m = re.search(regex, 'food,food,foo')
# print(m)
# m.group(1)
# m = re.search(regex, 'qux,qux')
# print(m)
# m.group(1)
# m = re.search(regex, 'foo,qux')
# print(m)

# aStr = 'abc'


# def recStr(aStr,sep):
# 	''' takes a string of len >=2
# 	returns a list of first and
# 	second items in string with separator
# 	in between'''
# 	k = aStr[0] + sep + aStr[1]
# 	aKeys = []
# 	aKeys.append(k)
	
# 	if len(aStr)==2:
# 		return aKeys
# 	else:
# 		return aKeys + recStr(aStr[1:],sep)

# print(recStr(aStr,'-'))


# import re
# astr = 'force of 5000 and 200'
# pat = r'.+ (\d+) .+ (\d+)'
# newStr = re.sub(pat,r'\1 and \2',astr)
# aList.append(newStr)

# print(newStr)


# def fac(num):
# 	print(num)
# 	if num == 0 or num == 1:
# 		return 1
# 	else:
# 		return num * fac(num-1)
   
# print(fac(4))

# x = lambda a : a + 10
# print(x(5))


# import datetime

# d1 = datetime.date(2022,4,8)
# days_later = d1 + datetime.timedelta(days=7)

# con_date = datetime.datetime.strftime(days_later,'%d/%m/%y')

# print(con_date)

# print(datetime.date.today())



# def countPat(aStr,pat):
# 	if len(aStr)<len(pat):
# 		return 0
# 	n=0
# 	if aStr[0:len(pat)]==pat:
# 		n+=1
# 	return n + countPat(aStr[1:],pat)

# s = 'azcbobobegghaklbobob'
# pattern = 'bob'
# print(countPat(s1,pattern))



# class puzzle(object):
#     def __init__(self, order):
#         self.label = order
#         for index in range(4):
#             if order[index] == '0':
#                 self.spot = index
#                 print('spot',self.spot)
#                 return None
#     def transition(self, to):
#         label = self.label
#         blankLocation = self.spot
#         newBlankLabel = str(label[to])
#         newLabel = ''
#         for i in range(4):
#             if i == to:
#                 newLabel += '0'
#             elif i == blankLocation:
#                 newLabel += newBlankLabel
#             else:
#                 newLabel += str(label[i])
#         return puzzle(newLabel)
#     def __str__(self):
#         return self.label


# c = puzzle('C0AB')

# print(c.transition(3))

# print(c)


# class Person:
#   name = "John"
#   age = 36
#   country = "Norway"

#   def getage():
#   	return age

# setattr(Person, 'age',40)
# #print(x)

# x = getattr(Person, 'age')
# print(x)

# class Dummy(object):
# 	pass
# d = Dummy()
# d.does_not_exist


# Python program to
# demonstrate __new__
  
# class A(object):
#     # new method returning a string
#     def __new__(cls):
#         print("Creating instance")
#         return "GeeksforGeeks"
  
# class B(object):
#     # init method returning a string
#     def __init__(self):
#         print("Initializing instance")
#         return "GeeksforGeeks"
  
# print(A())
# print(B())


# # assignment operators
# x = 12 # (00001100)
# y = 6  # (00000110)

# # The bin() function is used to print in binary format.

# print ('x =', x ,' and y =',y)
# # # and operator
# print ('x & y is equal to', bin(x & y))
# # # or operator
# print ('x | y is equal to', bin(x | y))
# # # xor operator 
# print ('x ^ y is equal to', bin(x ^ y))
# # # shift left operator
# print ('x << y is equal to', bin(x << y))
# # # shift right operator
# print ('x >> y is equal to', bin(x >> y))
# # # not operator
# print ('~ x is equal to', bin(~ x ))
# for i in range(0,3):
# 	print(i%2)

# generate all combinations of N items
# def powerSet(items):
#     N = len(items)
#     # enumerate the 2**N possible combinations
#     for i in range(2**N):
#         combo = []
#         for j in range(N):
#             # test bit jth of integer i
#             print(i,j)
#             print('i shift j',(i>>j))
#             if (i >> j) % 2 == 1:
#                 combo.append(items[j])
#         print(combo)
#         yield combo

# print(list(powerSet([2,3,4])))



# def baseb(n, b):
#     e = n//b
#     q = n%b
#     if n == 0:
#         return '0'
#     elif e == 0:
#         return str(q)
#     else:
#         return baseb(e, b) + str(q)


# print(fun(baseb(8,3)))

# print(int(baseb(1,3)))



# # generate all combinations of N items
# def powerSet2(items):
#     N = len(items)
#     # enumerate the 2**N possible combinations
#     for i in range(3**N):
#         bag1 = []
#         bag2 = []
#         combo = bag1,bag2
#         strI = baseb(i,3)
#         while len(strI)<len(items):
#         	strI = '0'+strI

#         for j in range(len(strI)):

#             if int(strI[j]) % 2 == 1:
#                 bag1.append(items[j])
#             elif (int(strI[j]) % 2 == 0 and int(strI[j]) != 0):
#             	bag2.append(items[j])

#         # print(combo)
#         yield combo

# print(list(powerSet2([2,3])))


# generate all combinations of N items
# def powerSet2(items):
#     N = len(items)
#     # enumerate the 2**N possible combinations
#     for i in range(3**N):
#         bag1 = []
#         bag2 = []
#         combo = bag1,bag2
#         strI = baseb(i,3)
#         while len(strI)<len(items):
#         	strI = '0'+strI

#         for j in range(len(strI)):

#             if int(strI[j]) % 2 == 1:
#                 bag1.append(items[j])
#             elif (int(strI[j]) % 2 == 0 and int(strI[j]) != 0):
#             	bag2.append(items[j])

#         # print(combo)
#         yield combo

# print(list(powerSet2([2,3])))

# s = 'azcbobobegghaklbegghh'
# print(len(s))

# def longestAlpha(aStr):
# 	longest = None
# 	txt = ''
# 	for i in range(len(aStr)-1):
# 		print('pl', aStr[i], i)
# 		txt = aStr[i]
# 		i+=1
# 		while (txt[-1] < aStr[i] or txt[-1] == aStr[i]):
# 			txt += aStr[i]
# 			i+=1
# 		print(txt)
# 		if longest==None:
# 			longest = txt
# 		elif len(txt) > len(longest):
# 			longest = txt
# 		print('longest', longest)
	
# 	return longest
	
# s = 'azcbobobegghaklbegghhjbob'
# s3 = 'azcbobobegghaklbegghhe'
# # print(longestAlpha(s))

# count = 0
# for i in range(1,len(s)):
# 	if s[i-1:i+2] == 'bob':
# 		count+=1

# print(count)

# str1 = 'exterminate!' 
# str2 = 'number one - the larch'

# print(str1.upper())

# print(str1)

# print(str1.isupper())

# print(str1.islower())

# str2 = str2.capitalize()
# print(str2.swapcase())
# print(str2)

# print(str1.index('e'))
# print(str2.index('n'))
# print(str2.find('n'))

# print(str2.find('!'))
# # print(str2.find('n'))
# print(str1.count('e'))

# str1 = str1.replace('e', '*')

# print(str1)

# print(str2.replace('one','seven'))

# def iterPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
 
#     returns: int or float, base^exp
#     '''
#     if exp == 0:
#         return 1
#     elif exp % 2 != 0:
#         return base
#     else:
#         return iterPower(base,exp//2)

# print(iterPower(2,2))


# def iterPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
 
#     returns: int or float, base^exp
#     '''
#     if exp == 0:
#     	return 1
#     ans = 1
#     while exp > 0:
#     	ans *= base
#     	exp-=1
#     return ans

# print(iterPower(2,5))

# def recurPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
 
#     returns: int or float, base^exp
#     '''
#     if exp == 0:
#     	return 1
#     elif exp %2 == 0:
#     	return recurPower(base*base,exp//2)
#     else:
#     	return base * recurPower(base*base, exp//2)

# print(recurPower(2,3))



# a = 'X-DSPAM-Confidence: 0.8475'
# print(''.join([e for e in a if e in '.0123456789']))
# # print(a.split(' ')[1])


# def isIn(char, aStr):
#     '''
#     char: a single character
#     aStr: an alphabetized string
    
#     returns: True if char is in aStr; False otherwise
#     '''
#     print(aStr)
#     if aStr == '':
#         return False
#     elif len(aStr) == 1:
#     	return aStr == char
#     else:
#         mid = int(len(aStr)/2)
#         print(aStr[mid])
#         if aStr[mid] == char:
#             return True
#         elif aStr[mid] > char:
#             aStr = aStr[0:mid]
#         else:
#             aStr = aStr[mid:]
#     return isIn(char, aStr)

# print(isIn('c','abcdef'))


# import pathlib

# print(pathlib.Path(__file__).parent)

# print((1, 2, (3, 'John', 4),'Hi')[0:1][0])

# listA = [1, 4, 3, 0]

# print(listA.sort())

# print(listA)

# print(listA.insert(0,100))

# print(listA.remove(3))

# print(listA.append(7))

# print(listA)

# listB = ['x', 'z', 't', 'q']

# print(listA + listB)

# print(listB.sort())
# print(listB.pop())
# print(listB.count('a'))
# print(listA.extend([4,1,6,3,4]))
# print(listA)
# print(listA.index(1))
# print(listA.pop(4))
# print(listA.reverse())
# print(listA)



# def applyEachTo(L, x):
#     result = []
#     for i in range(len(L)):
#         result.append(L[i](x))
#     return result


# def square(a):
#     return a*a

# def halve(a):
#     return a/2

# def inc(a):
#     return a+1

# print(applyEachTo([inc, square, halve, abs], 3.0))

# print(type(animals.keys()))

# print(animals)


# def lines(file):
# 	for line in file: yield line
# 	yield '\n'

# def blocks(file):
# 	block = []
# 	for line in lines(file):
# 		if line.strip():
# 			block.append(line)
# 		elif block:
# 			yield block
# 			block = []

# document = []
# def ListBlocks(file):
# 	for block in blocks(file):
# 		document.append(block)
# 	return document

# date = r'(\d+/\d+/\d+)'
# brothers = r'(.+): \(\d min.\) (.+) \((\d+)\) (.+)'
# sisters = r'(.+): \(\d min.\) (.+) \((\d+)\) (.+) Assistant: (.+)'
# # first = r'First Time: \(\d min.\) .+? \(\d+\)?'


# pats = [date,sisters,brothers]
# import sys
# sys.path.append(r'C:\Users\gnl999935\Documents\Python\SQL')

# from Create_sql_database import *

# import re

# # pats = []

# with open(r'C:\Users\gnl999935\Documents\schedule1.txt','r',encoding = 'utf8') as f:

# 	ass_list = []
# 	for l in f:
# 		for pat in pats:
# 			g = re.match(pat,l)
# 			#if we find a match that is a date
# 			if g:
# 				if len(g.groups()) == 1:
# 					#store current key
# 					curr_date = g.groups()[0]

# 				else:
# 					weeks_ass = []
# 					weeks_ass.append(curr_date)
# 					for e in g.groups():
# 						weeks_ass.append(e)
# 					if len(weeks_ass) == 5:
# 						weeks_ass.append('')
# 					ass_list.append(weeks_ass)
# 				break


# Table = ['Assignment']
# c1 = ('date type topic spech_quality student assistant').split()
# col = [c1]

# gen_sch('school db')
# gen_table(Table,col)


# InsV(ass_list,'Assignment')



# date = r'(\d+/\d+/\d+)'
# brothers = r'(.+): \(\d min.\) (.+) \((\d+)\) (.+)'
# sisters = r'(.+): \(\d min.\) (.+) \((\d+)\) (.+) ?(?:Assistant:) ?(.+)?'
# first = r'First Time: \(\d min.\) .+? \(\d+\)?'

# import re

# # pats = []
# bib = "Bible Reading: (4 min.) 2Sa 19:31-43 (2) Eze enoch"
# txt = "First Time: (3 min.) Use the topic wey dey the part ‘how we go preach this month.’ Then show wetin you go do when person for your territory give excuse why e no want accept the good news. (1) Amuta blessing Assistant: Kupolati Ebere"

# # print(re.match(sisters,txt_str).groups())
# print(re.match(sisters,txt).groups())


# with open(r'C:\Users\gnl999935\Downloads\S-140_E.docx','r',encoding='utf-8') as file:

# 	for e in file:
# 		print(e.strip())

# 
# n = '5 10'
# # for e in map(int,n.split(' ')):
# # 	print(e)
# dictn = {9:'a'}

# dictn_c = dictn.copy()
# print(dictn_c)
# import re
# pat = r"[100000-999999]{6}"

# print(re.match(pat,'100041'))


# import cmath
# import math
# # # s = 1+2j
# # # b = -1
# # # c = 0
# # # s1 = complex(s)
# # # print(s1)

# # # print(cmath.polar(s1))

# # print(math.sqrt(200)/2)

# val = math.asin(7.071/10)
# print(round(math.degrees(val)))

# if __name__ == '__main__':
#     import math
#     ab = 1
#     bc = 10
#     inside = math.pow(ab,2) + math.pow(bc,2)
#     print('i',inside)
#     hyp = math.sqrt(inside)
#     print('h', hyp)
#     val = math.asin((hyp/2)/bc)
#     print(val)
#     # print(round(math.degrees(val)))
#     # th = round(math.degrees(val))
#     print(f"{round(math.degrees(val))}\N{DEGREE SIGN}")

# theta = 45
# print(f"Theta {theta}\N{DEGREE SIGN}.")


# def timeConversion(s):
#     hr = int(s[0:2])
#     if s[-2:] == 'AM':
#         if hr == 12:
#             time = '00' + s[2:-2]
#         else:
#             time = s[0:-2]
#     else:
#         if hr == 12:
#             time = '12' + s[2:-2]
#         else:
#             time = str(hr + 12) + s[2:-2]
#     return time

# s = '12:40:00AM'

# print(timeConversion(s))

import itertools as it
# ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
# suits = ['H', 'D', 'C', 'S']

# # def cards():
# #     """Return a generator that yields playing cards."""
# #     for rank in ranks:
# #         for suit in suits:
# #             yield rank, suit

# # print(list(cards()))

# cards = it.product(ranks, suits)
# # print(list(cards))

# import random

# def shuffle(deck):
#     """Return iterator over shuffled deck."""
#     deck = list(deck)
#     random.shuffle(deck)
#     return iter(tuple(deck))

# cards = shuffle(cards)

# # print(list(cards))

# # def cut(deck, n):
# #     """Return an iterator over a deck of cards cut at index `n`."""
# #     if n < 0:
# #         raise ValueError('`n` must be a non-negative integer')

# #     deck = list(deck)
# #     return iter(deck[n:] + deck[:n])

# # cards = cut(cards, 26)  # Cut the deck in half.

# # print(list(cards))


# def cut(deck, n):
#     """Return an iterator over a deck of cards cut at index `n`."""
#     deck1, deck2 = it.tee(deck, 2)
#     top = it.islice(deck1, n)
#     bottom = it.islice(deck2, n, None)
#     # print(list(bottom))
#     # print()
#     # print(list(top))
#     # print(len(it.chain(bottom,top)))
#     return it.chain(bottom, top)

# cards = cut(cards, 26)

# # for e in [iter(cards)] *5:
# # 	for f in e:
# # 		print(f)

# # print(list(cards))
# # print()

# def deal(deck, num_hands=1, hand_size=5):
#     iters = [iter(deck)] * hand_size
#     # print(iters)
#     return tuple(zip(*(tuple(it.islice(itr, num_hands)) for itr in iters)))

# p1_hand, p2_hand, p3_hand = deal(cards, num_hands=3)

# print(p1_hand)
# print(p2_hand)
# print(p3_hand)

# print(len(tuple(cards)))


file = r'C:\Users\gnl999935\Documents\SP500.csv'


from collections import namedtuple

class DataPoint(namedtuple('DataPoint', ['date','value'])):
	__slots__ = ()

	def __le__(self, other):
		return self.value <= other.value

	def __lt__(self, other):
		return self.value <= other.value

	def __gt__(self, other):
		return self.value > other.value



import csv
from datetime import datetime

def read_prices(csvfile, _strptime = datetime.strptime):
	with open(csvfile) as infile:
		reader = csv.DictReader(infile)
		for row in reader:
			yield DataPoint(date = _strptime(row['Date'], '%Y-%m-%d').date(),
							value = float(row['Adj Close']))

prices = tuple(read_prices(file))
# for e in zip(prices[1:],prices):
# 	print(e)
	# break

gains = tuple(DataPoint(day.date, 100*(day.value/prev_day.value - 1.))
				for day, prev_day in zip(prices[1:],prices))

# print(gains)

import functools as ft

def consecutive_positives(sequence, zero=0):
    def _consecutives():
        for itr in it.repeat(iter(sequence)):
            yield tuple(it.takewhile(lambda p: p > zero,
                                     it.dropwhile(lambda p: p <= zero, itr)))
    return it.takewhile(lambda t: len(t), _consecutives())

growth_streaks = consecutive_positives(gains, zero=DataPoint(None, 0))

# print(growth_streaks)


longest_streak = ft.reduce(lambda x, y: x if len(x) > len(y) else y,
                           growth_streaks)

print(longest_streak)

