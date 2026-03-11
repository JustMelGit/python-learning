
from threading import Thread,Lock
from time import sleep

class database():
	def __init__(self):
		self.value = 0
		self.lock = Lock()


	def updateDatabase(self,increase):
		self.lock.acquire()
		currentValue = self.value
		currentValue+=increase
		sleep(0.1)
		self.value = currentValue
		print(f'counter {self.value}')
		self.lock.release()


c = database()

t1 = Thread(target = c.updateDatabase,args=(10, ))
t2 = Thread(target = c.updateDatabase,args=(5, ))


t1.start()
t2.start()

t1.join()
t2.join()

# print(c.updateDatabase(5))

print(f'final value of counter is {c.value}')

# from threading import Thread, Lock
# from time import sleep


# class Counter:
#     def __init__(self):
#         self.value = 0
#         self.lock = Lock()

#     def increase(self, by):
#         self.lock.acquire()

#         current_value = self.value
#         current_value += by

#         sleep(1)

#         self.value = current_value
#         print(f'counter={self.value}')

#         self.lock.release()


# counter = Counter()

# # create threads
# t1 = Thread(target=counter.increase, args=(10, ))
# t2 = Thread(target=counter.increase, args=(20, ))

# # start the threads
# t1.start()
# t2.start()


# # wait for the threads to complete
# t1.join()
# t2.join()


# print(f'The final counter is {counter.value}')