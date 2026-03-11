# from functools import wraps

# def make_blink(function):
# 	"""Defines the decorator"""

# 	#this makes the decorator trasparent in terms of its name and documentation
# 	@wraps(function)


# 	#Define the inner function

# 	def decorator():
# 		#Grab the return value of the function being decorated
# 		ret = function()


# 		#Add new functionality to the function being decorated
# 		return "<blink>" + ret + "</blink"
# 	return decorator


# #Apply the decorator here!
# @make_blink

# def hello_world():
# 	"""Original function!"""

# 	return "Hello, World!"

# #check the result of decorating
# print(hello_world())


# #Check if the function name is still the same name of the function being returned
# print(hello_world.__name__)


# #Check if the docstring is still the same as that of the function being returned
# print(hello_world.__doc__)


# def wrapper(f):
#     def fun(l):
#         f(l) 
#         # return f(l)
#         # print(val)
#         # if val.startswith('0'):
#         #     val = '+91'+val[1:]
#         # else:
#         #     val = '+91'+val
#         return val
#     return fun

# @wrapper
# def sort_phone(l):
#     print(*sorted(l), sep='\n')


# alist = [
# '07895462130',
# '919875641230',
# '9195969878'
# ]

# if __name__ == '__main__':
#     l = [input() for _ in range(3)]
#     sort_phone(l) 








# alist = ['Mike Thomson 20 M',
# 'Robert Bustle 32 M',
# 'Andria Bustle 30 F']

# # print(*alist,sep = '\n')

# dlist = [['Mike', 'Thomson', '20', 'M'],
# ['Robert', 'Bustle', '32', 'M'],
# ['Andria', 'Bustle', '30', 'F']]


# print(sorted(dlist,key = lambda x: (x[3],x[2],x[1],x[0])))

import calendar
print(calendar(2022))
b = calendar.TextCalendar()
calendar.TextCalendar.prmonth(b,2022,8)

print(calendar.TextCalendar.formatmonth(b,2022,8))

print(calendar.monthcalendar(2022,8))

print(int('08'))