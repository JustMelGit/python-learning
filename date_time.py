# inp = '08 05 2015'

# import calendar
# b = calendar.Calendar(0)
# month,day,year = map(int,inp.split())
# week_days = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
# val = calendar.weekday(year,month,day)
# print(val)
# print(week_days[int(val)])
# print('hello')

# import calendar
# b = calendar.Calendar()

# # print(b.yeardays2calendar(2023,4))




# import datetime
# t1 = 'Sun 10 May 2015 13:54:36 -0700'

# t3 = 'Sun May 10 13:54:36 2015'
# t2 = 'Sun 10 May 2015 13:54:36 -0000'

# print(datetime.datetime.strptime(t3,'%c'))





# def timeInWords(h, m):
# 	d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', \
# 	5 : 'five',6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',\
# 	11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',\
# 	15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',\
# 	19 : 'nineteen', 20 : 'twenty'}

# 	try:
# 		return d[m]
# 	except:
# 		_,m2 = divmod(m,20)
# 		return d[20]+'-'+d[m2]


# m = 25
# h = 7

# for i in range(30):
# 	print(timeInWords(7,i))

# print(timeInWords(h,m))



# def con_num_word(m):
#     d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
#           6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
#           11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
#           15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
#           19 : 'nineteen', 20 : 'twenty'}
    
#     try:
#         return d[m]
#     except:
#         _,m2 = divmod(m,20)
#         return d[20]+'-'+d[m2]
        
# def timeInWords(h, m):
#     if m == 0:
#         print(con_num_word(h),"o' clock")
#     elif 1 <= m <= 30:
#         if m == 15:
#             print('quarter past',con_num_word(h))
#         else:
#             print(con_num_word(m),'past',con_num_word(h))
#     else:
#         if m == 45:
#             print('quarter to',con_num_word(h+1))
#         else:
#             m = 60-m
#             print(m)
#             print(con_num_word(m),'to',con_num_word(h+1))



# timeInWords(1,1)







# import datetime,time

# x = datetime.datetime.now()

# time.sleep(5)

# y = datetime.datetime.now()

# print(y-x)

# from datetime import datetime

# alist = ['Sun 10 May 2015 13:54:36 -0700',
# 'Sun 10 May 2015 13:54:36 -0000',
# 'Sat 02 May 2015 19:54:36 +0530',
# 'Fri 01 May 2015 13:54:36 -0000']

# formated_date = datetime.strptime(alist[2],'%a %d %b %Y %X %z')
# formated_date1 = datetime.strptime(alist[3],'%a %d %b %Y %X %z')

# # delta = formated_date - formated_date1

# print(round((formated_date-formated_date1).total_seconds()))





# l = [
# 'GGGGGGG',
# 'GGGGGGG',
# 'GGGGGGG',
# 'GGGGGGG',
# 'GGGGGGG'
# ]

# def twoPluses(grid):
# 	#walk throgh grid
# 	# cnt = 0
# 	for i in range(len(grid[0])):
# 		for j in range(len(grid)):
# 			print(j,i)
# 			if grid[j][i] == 'G':
# 				 cnt = 0
# 				 top = j
# 				 bot = j
# 				 left = i
# 				 right = i
# 				 while 0 <= top < len(grid) and 0 <= bot < len(grid) and 0 <= left < len(grid) and 0 <= right < len(grid) and \
# 				 grid[top][i] == 'G' and grid[bot][i] == 'G' and grid[j][left] == 'G' and grid[j][right] == 'G':
# 				 	top -= 1 
# 				 	bot += 1
# 				 	left -= 1
# 				 	right += 1
# 				 	print(top,bot,left,right)
# 				 	cnt += 1
				 

# 	return cnt

# 	#create boundaries
# 	#ensure no clashes
# 	#when you find a bigger cross replace cross boundaries
# 	#Replace for both biggest and second biggest
# 	#return multiple of two boundaries 

# print(twoPluses(l))

def len_of_dash(strg):
	i = 0
	while strg[i] == '-':
		i += 1
	leng = i + 1
	return leng,i 




def crosswordPuzzle(crossword, words):
	for lines in crossword:
		for i,el in enumerate(lines):
			if lines[i] == '-':
				#get length of dash
				print(i,lines[i])




cross = ['adb--kbs']
words = ['joy']

# crosswordPuzzle(cross,words)

s = ['--kbs']

print(len_of_dash(s))