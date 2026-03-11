# full_names = (name.strip() for name in open(r'C:\Users\Justice\Documents\names.txt'))
# lengths = ((name,len(name)) for name in full_names)
# longest = max(lengths,key=lambda x:x[1])
# print(longest)


# def separate_names(names):
# 	for full_name in names:
# 		for name in full_name.split(' '):
# 			yield name



# full_names = (name.strip() for name in open(r'C:\Users\Justice\Documents\names.txt'))
# names = separate_names(full_names)
# lengths = ((name,len(name)) for name in full_names)
# longest = max(lengths,key=lambda x:x[1])
# print(longest)

# def get_longest(namelist):
# 	full_names = (name.strip() for name in open(namelist))
# 	names = separate_names(full_names)
# 	lengths = ((name,len(name)) for name in names)
# 	return list(lengths)
# 	return max(lengths,key=lambda x:x[1])



# print(get_longest(r'C:\Users\Justice\Documents\names.txt'))


# @contextmanager
# def simple_context_manager(obj):
# 	try:
# 		#do something
# 		yield
# 	finally:
# 		#wrap up

from contextlib import contextmanager
@contextmanager
def simple_context_manager(obj):
	try:
		obj.some_property+=1
		yield
	finally:
		obj.some_property-=1

class some_obj(object):
	def __init__(self,arg):
		self.some_property = arg

obj = some_obj(5)
print(obj.some_property)



with simple_context_manager(obj):
	print(obj.some_property)


from time import time
HEADER = 'this is the header \n'
FOOTER = '\nthis is the footer \n'

@contextmanager
def new_log_file(name):
	try:
		logname = name
		f = open(logname, 'w')
		f.write(HEADER)
		yield f
	finally:
		f.write(FOOTER)
		print('logfile created')
		f.close()

# with new_log_file(r'C:\Users\Justice\Desktop\log.txt') as file:
# 	file.write('this is the body')

# def coroutine_example():
# 	while True:
# 		x = yield
# 		#do something with x
# 		print(x)

# c = coroutine_example()
# c.__next__()
# c.send(10)

# def counter(string):
# 	count = 0
# 	try:
# 		while True:
# 			item = yield
# 			if isinstance(item,str):
# 				if item in string:
# 					count+=1
# 					print(item)
# 				else:
# 					print('No match')
# 			else:
# 				print('Not a string')
# 	except GeneratorExit:
# 		print(count)


# c = counter('Jane')
# c.__next__()
# c.send('Ja')
# c.send('ane')

def couroutine_decorator(func):
	def wrap(*args,**kwargs):
		cr = func(*args,**kwargs)
		cr.__next__()
		return cr
	return wrap

@couroutine_decorator
def couroutine_example():
	while True:
		x = yield
		#do some_property with x
		print(x)

c = couroutine_example()
c.send('success')

def sender(filename,target):
	for line in open(filename):
		target.send(line)
	target.close()

@couroutine_decorator
def match_counter(string):
	count = 0
	try:
		while True:
			line = yield
			if string in line:
				count+=1
	except GeneratorExit:
		print('{}:{}'.format(string,count))


c = match_counter('NORUO')
sender(r'C:\Users\Justice\Documents\names.txt',c)


@couroutine_decorator
def longer_than(n):
	count = 0
	try:
		while True:
			line=yield
			if len(line)>n:
				print(line)
				count+=1
	except GeneratorExit:
		print('longer than {}: {}'.format(n,count))

l = longer_than(14)
sender(r'C:\Users\Justice\Documents\names.txt',l)


@couroutine_decorator
def router():
	try:
		while True:
			line = yield
			first,last = line.split(' ')
			fnames.send(first)
			lnames.send(last.strip())
	except GeneratorExit:
		fnames.close()
		lnames.close()


@couroutine_decorator
def file_write(filename):
	try:
		with open(filename,'a') as file:
			while True:
				line = yield
				file.write(line+'\n')
	except GeneratorExit:
		file.close()
		print('one file created')

if __name__ == '__main__':
	fnames = file_write(r'C:\Users\Justice\Desktop\first_names.txt')
	lnames = file_write(r'C:\Users\Justice\Desktop\last_names.txt')
	router = router()
	for name in open(r'C:\Users\Justice\Documents\names.txt'):
		router.send(name)
	router.close()