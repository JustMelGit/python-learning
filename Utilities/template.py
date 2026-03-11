

# import sys
# #args = sys.argv[1:]
# args = sys.argv
# #args.reverse()
# print (args)


# errno = 50159747054
# name = 'Bob'
# girl = 'Jane'
# print('Hello, %s' % name)

# print('%x' % errno)

# print('Hey %s, there is a 0x%x error!' % (name, errno))

# print('Hey %(name)s, there is a 0x%(errno)x error!' % {"name": name, "errno": errno })


# print('Hello, {}'.format(name))
# print('hi {0:-12}\t {2:20.2f}\t'.format(100,550,600))


# print('Hey {name}, there is a 0x{errno:x} error!'.format(name=name, errno=errno))

# print(f'Hello, {name}!')

# a = 5
# b = 10
# print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')


# def greet(name, question):
# 	return f"Hello, {name}! How's it {question}?"

# print(greet('Bob', 'going'))


# def greetings(name, question):
# 	return "Hello, " + name + "! How's it " + question + "?"

# print(greetings('Bob', 'going'))

# print(f"Hey {name}, there's a {errno:#x} error!")


# from string import Template

# t = Template('Hey, $name!')
# t.substitute(name=name)


# templ_string = 'Hey $name, there is a $error error!'
# print(Template(templ_string).substitute(name=name, error=hex(errno)))




# # This is our super secret key:
# SECRET = 'this-is-a-secret'

# class Error:
# 	def __init__(self):
# 		pass

# # A malicious user can craft a format string that
# # can read data from the global namespace:
# user_input = '{error.__init__.__globals__[SECRET]}'

# # This allows them to exfiltrate sensitive information,
# # like the secret key:
# err = Error()
# print(user_input.format(error=err))


# user_input = '${error.__init__.__globals__[SECRET]}'
# Template(user_input).substitute(error=err)

# with open(r'C:\Users\Justice\Documents\post hnd student.txt','r') as f:
# 	data = f.read()

# with open(r'C:\Users\Justice\Documents\Practice.txt','w') as g:
# 	g.write(data)

# from os import scandir
# from datetime import datetime
# def convert_date(timestamp):
# 	d = datetime.utcfromtimestamp(timestamp)
# 	formated_date = d.strftime('%d %b %y')
# 	return formated_date



# def get_files():
# 	dir_entries = scandir(r'C:\Users\Justice\Documents')
# 	for entry in dir_entries:
# 		if entry.is_file():
# 			info = entry.stat()
# 			print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')

# get_files()

# lists = ['cat','goat','cow']

# print(''.join(lists))

# file = open(r'C:\Users\Justice\Documents\newfile.txt'))

# def lines(file):
# 	for line in file:
# 		print(line)



# for e in file:
# 	try:
# 		print(e)
# 	except UnicodeDecodeError:
# 		print('',end='')

# emotion_dict = {1:['a','b','d'],2:'b',3:'c'}


# em = {x for y in emotion_dict.values() for x in y}

# eml = [x for y in emotion_dict.values() for x in y]



# print(em)
# print(eml)
# print(emotion_dict.get(1))


