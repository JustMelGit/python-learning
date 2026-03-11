# even = []
# odd = []
# for i in range(1,101):
# 	if i%2==0:
# 		even.append(i)
# 	else:
# 		odd.append(i)

# print(even)
# print(odd)


# def per(aStr):
# 	if len(aStr)==1:
# 		yield (aStr[0])
# 	else:
# 		for l in range(len(aStr)):
# 			for n in per(aStr[:l] + aStr[l+1:]):
# 				yield aStr[l] + n
# # print(list(per('ABCD')))

# def pairs(aStr):
# 	if len(aStr)==2:
# 		return [aStr[0:2][::-1]]
# 	else:
# 		return [aStr[0:2][::-1]] + pairs(aStr[1:])


# def edges(aStr):
# 	for e in pairs(aStr):
# 		pos = aStr.index(e[::-1])
# 		if pos==0:
# 			e = e + aStr[2:]
# 		elif pos==len(aStr)-2:
# 			e = aStr[0:-2] + e
# 		elif pos>0 and pos<len(aStr)-2:
# 			e = aStr[0:pos]+e+aStr[pos+2:]
# 		print(aStr,'-',e)

# edges('ABCDE')

# s = 'foo123bar'
# y = re.search('123',s)

# for e in y:
# 	print(e)

# print(y)

# print(s[3:6])

# print(re.search('\W', '#(.a$@&'))

# print(re.match('foo[1-9]?bar', 'foo2bar'))

# for i in range(1,6):
# 	s = f"x{'-'* i}x"
# 	print(f'{i} {s:10}', re.search('x-{2,4}x',s))

# m = re.search('(bar)+', 'foo barbarbarbar baz')
# print(m.group(1))

# m = re.search(r'(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,quux,baz')
# print(m.groups())

# m = re.search(r'(\w+),\1', 'foo,foo')
# print(m)

# import re

# s = '"Python\'s awsome". She said'
# pattern = r'([\'"])(.*?)\1'

# match = re.search(pattern, s)
# print(match.group(0))

# s = '"Python\'s awsome". She said'
# pattern = '[\'"].*?[\'"]'

# match = re.search(pattern, s)

# print(match.group(0))

# pat = '(bar)+ baz'
# m = re.search(r'(foo(bar)?)+(\d\d\d)?', 'foofoobar')
# # print(m)
# print(m.groups())

# regex = r'(\w+),\1'

# m = re.search(regex,'foo,foo,foo')

# print(m)

# file = open(r'C:\Users\gnl999935\Documents\Python\May 2022.txt','r',encoding='utf8')



# pat = r'Bible Reading: \(\d min\.\) [\d]Sa [\d]+:[\d]+-[\d]+ \(\d\).*?'
# for f in file:
# 	# print(f)
# 	m = re.match(pat,f)
# 	if m:
# 		print(m.group(0))



# prev = {0:0,1:1}
# def fib(n):
# 	if n in prev.keys():
# 		return prev[n]
# 	else:
# 		fi = fib(n-1) + fib(n-2)
# 		prev[n] = fi
# 		return fi
# fib(3)
# print(prev)

# fact = {0:0,1:1}
# def fac(n):
# 	if n in fact.keys():
# 		return fact[n]
# 	else:
# 		fa = n*fac(n-1)
# 		fact[n] = fa
# 		return fa

# print(fac(5))
# print(fact)

# aStr = 'https://nairaland.com/	https://www.nairaland.com/7055394/kyari-rejects-prison-food-inmates'


# file = open(r'C:\Users\gnl999935\Documents\foundurls1.txt','r')
# pat = r'.+//?(.+)$'
# for e in file:
# 	m = re.search(pat,e)
# 	if m:
# 		st = m.group(1)
# 		if '-' in st:
# 			story = re.sub('-',' ',st)
# 			print(story)

print(1//2)