class Meta(type):
	def __new__(self, class_name, bases, attrs):
		print(attrs)
		a = {}
		for name,val in attrs.items():
			if name.startswith("__"):
				a[name] = val
			else:
				a[name.upper()] = val
		return type(class_name, bases,a)


class Dog(metaclass=Meta):
	x = 5
	y = 8

	def hello(self):
		print('hi')

d = Dog()
print(d.HELLO())