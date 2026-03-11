# import requests
# from bs4 import BeautifulSoup
# import re


# URL = 'https://www.jobberman.com/jobs/engineering-technology/lagos'
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find(class_="search-main__content")
# job_elems = results.find_all('article', class_='search-result')

# for job_elem in job_elems:
# 	title_elem = job_elem.find('h3')
# 	location_elem = job_elem.find('div', class_='search-result__location')
# 	salary_elem = job_elem.find('div', class_='search-result__job-salary')
# 	link = job_elem.find('a')['href']
# 	if None in (title_elem,location_elem,salary_elem):
# 		continue
# 	print(title_elem.text)
# 	print(location_elem.text)
# 	print(location_elem.text)
# 	print(link)
# 	print()





# URL = 'https://guardian.ng/'
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find(class_="news-headline")
# headlines = results.find_all('div', class_="headline")
# for headline in headlines:
# 	link = headline.find('a')['href']
# 	print(headline.text)
# 	print(link)
# print('\n')



# # URL = 'https://guardian.ng/'
# # page = requests.get(URL)
# # soup = BeautifulSoup(page.content, 'html.parser')
# # results = soup.find(class_="category design-article")


# # headlines = results.find_all('div', class_="cell")
# # for headline in headlines:
# # 	if None in headlines:
# # 		continue

# # 	link = headline.find('a')['href']
# # 	print(headline.text)
# # 	print(link)


# URL = 'https://realpython.com/python-string-formatting/'
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')
# article = soup.find_all("p")
# for e in article:
# 	print(e.text)


# URL = 'https://www.tripadvisor.com/Restaurants-g304026-c10646-Lagos_Lagos_State'
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find(class_="_1kXteagE")
# # print(results)
# job_elems = results.find_all(class_="_1llCuDZj")
# Reviews = {}
# pat = '.+\-(.+)\-.+'
# # job_elems = results.find_all(class_="wQjYiB7z")

# for job_elem in job_elems:

# 	link = (job_elem.find('a')['href'])
# 	m = re.search(pat,link)

# 	# review = (job_elem.find(class_="_3mPt7dFq"))
# 	# link = class_="wQjYiB7z"


# 	# link = job_elem.find('a')['href']
# 	# if None in (link):
# 	# 	continue
	
# 	# print(review.text)
# 	# print(location_elem.text)
# 	# print(location_elem.text)
# 	Reviews[m.group(1)]=[link]
# 	m = ''

# for k in Reviews:

# 	URL = 'https://www.tripadvisor.com' + Reviews[k][0]

# 	page = requests.get(URL)
# 	soup = BeautifulSoup(page.content, 'html.parser')
# 	results = soup.find(class_="listContainer hide-more-mobile")
# 	ind = results.find_all(class_="entry")
# 	for e in ind:
# 		Reviews[k].append(e.text)
# print(Reviews)




# article = results.find_all("p")
# for e in article:


# f = r'C:\Users\gnl999935\Documents\plates.txt'

# doc = open(f,'r',encoding='utf8')
# lst = []
# for plate in doc:
# 	lst.append(plate[0:4])

# from collections import Counter

# plate_cnt = Counter(lst)
# for plate,count in plate_cnt.items():
# 	print(plate,count)



# from itertools import combinations_with_replacement

# lst = []
# for e in combinations_with_replacement([10,100],3):
# 	e = list(e)
# 	e[0] = 10
# 	lst.append(e)
# for e in lst:
# 	for i in range(1,len(e)):
# 		e[i] = e[i]+e[i-1]


# print(lst)



# print(list(combinations_with_replacement([100,10],3)))
# bought_cost = [10.0,12.55,17.99]
# sale_price = [12.0,11.50,20.0,1]

# # profit_loss = 0
# # for sales,cost in zip(sale_price,bought_cost):
# # 	profit_loss += sales-cost
# # if profit_loss > 0:
# # 	print('Profit',profit_loss)
# # else:
# # 	print('loss',profit_loss)


# profit_loss = 0
# for i in range(len(sale_price)):
# 	profit_loss += sale_price[i]-bought_cost[i]
# if profit_loss > 0:
# 	print('Profit',profit_loss)
# elif profit_loss < 0:
# 	print('loss',profit_loss)
# else:
# 	print('No profit and no loss',profit_loss)


# student_records = {
# 	'Ada': 98.0,
# 	'Bill': 45.0,
# 	'Charlie': 63.2

# }

# student_names = ['Neva','Kelly','Emerson']
# student_grades = [72.2,64.9,32.0]
# #check if the len of student names and len of grades are equal.
# #if not it will throw an error saying 'not the same' 
# assert len(student_names) == len(student_grades),'not the same'

# for i in range(len(student_names)):
# 	student_records[student_names[i]] = student_grades[i]
# print(student_records)



# bought_cost = [10.0,12.55,17.99]
# sale_price = [12.0,11.50,20.0,1]

# profit_loss = 0
# for sales,cost in zip(sale_price,bought_cost):
# 	profit_loss += sales-cost
# if profit_loss > 0:
# 	print('Profit',profit_loss)
# else:
# 	print('loss',profit_loss)


# bought_cost = [10.0,12.55,17.99]
# sale_price = [12.0,11.50,20.0]
# profit_loss = 0
# for i in range(len(sale_price)):
# 	profit_loss += sale_price[i]-bought_cost[i]
# if profit_loss > 0:
# 	print('Profit',profit_loss)
# elif profit_loss < 0:
# 	print('loss',profit_loss)
# else:
# 	print('No profit and no loss',profit_loss)


# bought_cost = [10.0,12.55,17.99]
# sale_price = [12.0,11.50,20.0]

# profit_loss = 0
# for sales,cost in zip(sale_price,bought_cost):
# 	profit_loss += sales-cost
# if profit_loss > 0:
# 	print('Profit',profit_loss)
# else:
# 	print('loss',profit_loss)

d = {}
d['e'] = 'g'
print(d)