# if __name__ == '__main__':
#     n = int(input())
#     from collections import namedtuple
#     report = namedtuple('report',input())
#     marks = []
#     for i in range(n):
#         student = report(*input().split())
#         marks.append(int(student.MARKS))
#     print('{:.2f}'.format(sum(marks)/n))



#name tuple

# from collections import namedtuple
# Car = namedtuple('Car','Price Mileage Colour Class')
# xyz = Car(10000,30,'Cyan','Y')
# print(xyz.Price)




# from collections import deque

# for _ in range(int(input())):  
#     _, queue =input(), deque(map(int, input().split()))
    
#     for cube in reversed(sorted(queue)):
#         if queue[-1] == cube: queue.pop()
#         elif queue[0] == cube: queue.popleft()
#         else:
#             print('No')
#             break
#     else: print('Yes')




# from collections import deque
# a = [3,4,5]
# a_d = deque(a)

# a_d.rotate(-1)
# print(a_d)