# def couroutine_decorator(func):
# 	def wrap(*args,**kwargs):
# 		cr = func(*args,**kwargs)
# 		cr.__next__()
# 		return cr
# 	return wrap


def decor(f):
	def wrapper(*args,**kwargs):
		print('Started')
		rv = f(*args,**kwargs)
		print('Ended')
		return rv
	return wrapper

@decor
def func2(x,y):
	print(x)
	print(y)
	return x,y

x = 2
y = 3

print(func2(x,y))

# @decor
# def func3():
# 	print("i am func3")

# func3()
# # x= func2(5,6)
# # print(x)

# import time
# def timer(func):
# 	def wrapper(*args, **kwargs):
# 		start = time.time()
# 		rv = func()
# 		total = time.time()-start
# 		print("Time:", total)
# 		return rv
# 	return wrapper

# @timer
# def test():
# 	for e in range(1000000):
# 		pass

# test()

print('1'>'2')