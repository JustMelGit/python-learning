# import random
# def genEven():
# 	'''
# 	Returns a random even number x, where 0 <= x < 100
# 	'''
# 	numbers = [number for number in range(2,100) if number%2==0]
# 	choice = random.choice(numbers)
# 	return choice

# print(genEven())

# import random
# def deterministicNumber():
#     '''
#     Deterministically generates and returns an even number between 9 and 21
#     '''
#     numbers = [number for number in range(9,21) if number%2==0]
#     return numbers[0]

# print(deterministicNumber())


# import random
# def stochasticNumber():
#     '''
#     Stochastically generates and returns an even number between 9 and 21
#     '''
#     numbers = [number for number in range(9,21) if number%2==0]
#     choice = random.choice(numbers)
#     return choice

# print(stochasticNumber())


# max_num = float("-inf")
# print(max_num)


# import random
# def dist1():
#     return random.random() * 2 - 1

# def dist2():
#     if random.random() > 0.5:
#         return random.random()
#     else:
#         return random.random() - 1 


# print(random.random()*2)
# print(dist2())


import random

# def dist3():
#     return int(random.random() * 10)

# def dist4():
#     return random.randrange(0, 10)


# trials = 1000
# for i in range(trials):
# 	if random.randint(0,10) == 0:
# 		print(i)
# 		print ('True')
# 		break
# # print ('False')


# def dist6():
#     return random.randint(0, 10)



# d1 = {}
# for i in range(10000):
#     x = random.randrange(10) 
#     d1[x] = d1.get(x, 0) + 1


import random
# mylist = []

# for i in range(random.randint(1, 10)):
# 	print(i)
# 	random.seed(0)
# 	if random.randint(1, 10) > 3:
# 		number = random.randint(1, 10)
# 		mylist.append(number)
# print(mylist)

# Code Sample A
mylist = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        if number not in mylist:
            mylist.append(number)
# print(mylist)

    
    
# Code Sample B
mylist = []

random.seed(0)
# for i in range(random.randint(1, 10)):
#     if random.randint(1, 10) > 3:
#         number = random.randint(1, 10)
#         mylist.append(number)
# print(mylist)

print(random.randint(1,10))