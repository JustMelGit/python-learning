# s = 'azcbobobegghakl'

# s = 'abcdabcdef'
# walk through s
# if the str in front is greater than behind, count,add the string to l str
	# if the cnt is greater than current longest, update
#else update str to cur str, update cnt


# walk through s
# set pointer
# if the no in front is greater increase cont by one
# else check if len of s[pointer:i+1] is greater than cur lng update lng, set pointer at i
# else set pointer

# cnt = 1
# pointer = 0
# lng = s[0]
# for i in range(1,len(s)):
# 	if s[i] > s[i-1]:
# 		cnt+=1
# 		if i+1 == len(s):
# 			break
# 	else:

# 		# print(cnt)
# 		if cnt > len(lng):
# 			lng = s[pointer:i]
# 		else:
# 			lng = s[i]
# 		cnt = 1
# 		pointer = i
# print()


# seq = [2,3,6,6,5]

# seq.sort()

# print(seq)


# def countdown(n):
# 	# print(n)
# 	if n>0:
# 		countdown(n-1)
# 	print('n',n)

# countdown(3)


# def factorial(n):
# 	print(f"factorial({n})")
# 	if n<=1:
# 		result = 1
# 	else:
# 		result = n*factorial(n-1)
# 	print('returning result', result)
# 	return result

# 	# result = 1 if n <= 1 else n * factorial(n-1)
# 	# print('returning', result)
# 	# return result

# print(factorial(4))

# seq = [1,2,3]
# seq1 = [4,5,6]

# import itertools as it
# print(*list(it.product(seq,repeat = 2)))

# s = 'HACK'
# items = [''.join(e) for e in it.permutations(s,2)]
# items.sort()

# print(*items,sep='\n')


# print(*list(it.permutations(s,2)))


# from itertools import combinations_with_replacement,combinations

# print(list(combinations(seq,2)))

# print(list(combinations_with_replacement(seq,2)))
# import collections as cl

# from collections import namedtuple
# Car = cl.namedtuple('Car','Price Mileage Colour Class')
# xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
# print (xyz)

# print (xyz.Class)



# from collections import namedtuple
# Car = namedtuple('Car','Price Mileage Colour Class')
# xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
# print (xyz)

# print (xyz.Class)



# n = 20

# if n %2 != 0:
# 	print('Weird')
# if n % 2 == 0 and 2 <= n <= 5:
# 	print('Not Weird')
# if n % 2 == 0 and 6 <= n <= 20:
# 	print('Weird')
# if n % 2 == 0 and n > 20:
# 	print('Weird')



# arr = [2,3,5,-1,-2,0]

# def plusMinus(arr):
# 	n = len(arr)
# 	ps_cnt,ng_cnt,ze_cnt = 0,0,0
# 	for e in arr:
# 		if e < 0:
# 			ng_cnt += 1
# 		elif e > 0:
# 			ps_cnt += 1
# 		else:
# 			ze_cnt += 1
# 	print(f'{ps_cnt/n:.6f}\n{ng_cnt/n:.6f}\n{ze_cnt/n:.6f}')


# plusMinus(arr)



# CrossWord Puzzle
# def crossWordPuzzle(crossword,words):
# 	r = 0
# 	while r < len(crossword):
# 		c = 0
# 		while c < len(crossword[r]):
# 			if crossword[r][c] == '-':
# 				print('h',r,c)
# 				i = c
# 				j = r
# 				while i < len(crossword[r]) and crossword[r][i] == '-':
# 					i+=1
# 				while j < len(crossword) and crossword[j][c] == '-':
# 					j+=1
# 				print(r,c,i,j)
# 				# return

# 			c+=1
# 		r+=1


# crosswords = [
# '++++++++++',
# '+------+++',
# '+++-++++++',
# '+++-++++++',
# '+++-----++',
# '+++-++-+++',
# '++++++-+++',
# '++++++-+++',
# '++++++-+++',
# '++++++++++']

# words = [
# 'POLAND'
# 'LHASA'
# 'SPAIN'
# 'INDIA'
# ]

# crossWordPuzzle(crosswords,words)

# 2. when you see a dash
#    2.1 get the length of the dash vertically or horizonally
#    2.2 determine if dash is vertical or horizontal
# 3. Check if we can fit a word from words - check every possibility
#    3.1 Determine whether subscript or complete word should be added
#        3.1.1  if the word is precided by a plus - add complete word and remove from list
#        3.1.1 if the word is precided by an alphabet - determine alphabet already
#              available - check for subcripts in words and add remaining slice - remove from list
# 4. Get current position of row and column
# 5. Pass newcrossword,position,and word to new recursive call 

# sub = ''
# rem = '----'
# subRem = sub+rem
# txt = 'jane'
# print(txt.startswith(sub) and len(txt)==len(subRem))





# Crossword Puzzle

# 1. walk through cross words

def crossWordPuzzle(crossword,words,r=0,d=0):
	print(*crossword,sep='\n')
	print()
	if len(words) == 0:
		return crossword
	from string import ascii_uppercase
	# r = 0
	while r < len(crossword):
		c = 0

		while c < len(crossword[r]):
			if crossword[r][c] == '-':
				i = c
				i_cnt = 0
				j = r

				while i < len(crossword[r]) and (crossword[r][i] == '-' or crossword[r][i] in ascii_uppercase):
					i+=1
					i_cnt += 1
				
				j_cnt = 0
				while j < len(crossword) and (crossword[j][c] == '-' or crossword[j][c] in ascii_uppercase):
					j+=1
					j_cnt += 1
				
				if j_cnt > i_cnt:
					pos = r-1
					sub = ''
					while crossword[pos][c] in ascii_uppercase and pos >= 0:
						sub += crossword[pos][c]
						pos -= 1

					wordlist = []
					for word in words:
						if word.startswith(sub) and len(word)==len(sub)+j_cnt:
							wordlist.append(word)

					for e in wordlist:
						e_d = e[len(sub):]
						for k in range(j_cnt):
							new_crossword = crossword
							new_words = words
							new_crossword[r+k] = new_crossword[r+k][:c] + e_d[k] + new_crossword[r+k][c+1:]
						new_words.remove(e)
						crossWordPuzzle(new_crossword,new_words,r,c+1)
				else:
					pos_h = c-1
					sub_h = ''
					while crossword[r][pos_h] in ascii_uppercase and pos_h >= 0:
						sub_h += crossword[r][pos_h]
						pos_h -= 1

					wordlist_h = []
					for word in words:
						print(sub_h,i_cnt)
						if word.startswith(sub_h) and len(word)==len(sub_h)+i_cnt:
							# print('word',word)
							wordlist_h.append(word[len(sub_h):])

					print(wordlist_h,words)
					for word in wordlist_h:
						new_crossword = crossword
						new_words = words
						new_crossword[r] = new_crossword[r][:c] + word + new_crossword[r][len(new_crossword[r][:c])+len(word):]
						new_words.remove(sub_h+word)
						crossWordPuzzle(new_crossword,new_words,r,c+len(word))
			c+=1
		r+=1

# crosswords = [
# '++++++++++',
# '+------+++',
# '+++-++++++',
# '+++-++++++',
# '+++-----++',
# '+++-++-+++',
# '++++++-+++',
# '++++++-+++',
# '++++++-+++',
# '++++++++++']

# words = [
# 'POLAND',
# 'LHASA',
# 'SPAIN',
# 'INDIA'
# ]


# crosswords1 = [
# '+-++++++++',
# '+-++++++++',
# '+-++++++++',
# '+-----++++',
# '+-+++-++++',
# '+-+++-++++',
# '+++++-++++',
# '++------++',
# '+++++-++++',
# '+++++-++++']

# words1 = [
# 'LONDON',
# 'DELHI',
# 'ICELAND',
# 'ANKARA']


# crosswords2 = [
# '+-++++++++',
# '+-++++++++',
# '+-------++',
# '+-++++++++',
# '+-++++++++',
# '+------+++',
# '+-+++-++++',
# '+++++-++++',
# '+++++-++++',
# '++++++++++']


# words2 = [
# 'AGRA',
# 'NORWAY',
# 'ENGLAND',
# 'GWALIOR']


crosswords3 = [
'++++++-+++',
'++------++',
'++++++-+++',
'++++++-+++',
'+++------+',
'++++++-+-+',
'++++++-+-+',
'++++++++-+',
'++++++++-+',
'++++++++-+']

words3 = [
'ICELAND',
'MEXICO',
'PANAMA',
'ALMATY']


crosswords4 = [
'+-++++++++',
'+-++-+++++',
'+-------++',
'+-++-+++++',
'+-++-+++++',
'+-++-+++++',
'++++-+++++',
'++++-+++++',
'++++++++++',
'----------']



# words4 = 'CALIFORNIA;NIGERIA;CANADA;TELAVIV'.split(';')


# print(*crossWordPuzzle(crosswords4,words4),sep = '\n')


def leap_year(year):
	leap = false
	if year%4 == 0:
		if year%100 == 0:
			if year%400 == 0:
				leap = 'True'
			return leap
		leap = 'True'
	return leap

