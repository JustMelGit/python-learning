class Person:
	def __init__(self,name):
		self.name = name
	def __repr__(self):
		return f'person({self.name})'
	def __mul__(self,x):
		if type(x) is not int:
			raise Exception("invalid argument, must be int")
		return self.name.upper() *x
	def __call__(self,y):
		print("called this function", y)
	def __len__(self):
		return len(self.name)*2

P = Person('tim')
print(len(P))

print(P*2)
print(P)

from queue import Queue as q
import inspect

class Queue(q):
	def __repr__(self):
		return f"Queue({self._qsize()})"
	def __add__(self, item):
		self.put(item)
	def __sub__(self,item):
		self.get()
qu = Queue()
qu + 9
qu + 7
qu - None
print(qu)
print(qu)

class Foo:
	def show(self):
		print("hi")

Test = type('Test', (Foo,), {"x":5})
t = Test()
t.wy = 'hello'
print(t.show())
print(t.wy)
t.show()


