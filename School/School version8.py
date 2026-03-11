import re

def lines(file):
    f = open(file,'r',encoding='utf-8')
    for line in f: yield line
    yield 'Bible Reading'
    f.close()

def blocks(file):
    block = []
    for line in lines(file):
        if not line.startswith('3. Bible Reading'):
            block.append(line.strip())
        elif block and line.startswith('3. Bible Reading'):
            yield ' '.join(block)
            block = [line.strip()]


def recurFind(pat,aStr,items = []):
    if pattern.search(aStr)==None:
        return(items)
    m = pattern.search(aStr)
    if m:
        loc = m.span(0)
        item = aStr[loc[0]:loc[1]]
        items.append(item)
        recurFind(pat,aStr[loc[1]:],items)
    return items


def monthParts(pat,files):
    months = {}
    l = 0
    for e in list(blocks(files)):
        m = recurFind(pat,e,[])
        months[l] = m
        l+=1
    return months


file =r'C:\Users\HP\Documents\july-august.txt'
pattern = re.compile(r'(3. Bible Reading|First Time|Return Visit|Bible Study|Talk): \(\d min.\) .+? \(\d+\)?')


g = monthParts(pattern,file)


bible_reading = [
'Eze enoch',
'Aimiehino orobosa',
'Agbamu Harmony',
'Maina John',
'Oriki Israel',
'Onoja Friday',
'Barak Andreson',
'Smart Joegodson']

firstime = [
'Amuta blessing',
'Erodu kindness',
'Annabel Nwabueze',
'Oghenetejiri Mario',
'Siyuna John',
'Ighavodha Amber',
'Ighavodha Annabel',
'Onoja Ojoma',
'Agbamu Harvest']


return_visit = [
'Ighavodha Doreen',
'Ubong pascaline',
'Aimiehino cecilia',
'Aimiehino augusta',
'Hoedjakou jael',
'Sarah Onyibe',
'Kupolati Ebere',
'Agbamu Patience',
'Oluwaseyi Blessing',
'Onoja Chiamaka',
'Udoh Glory Ezekiel']


bible_study =[
'Igbiya Confidence',
'Obarah Grace',
'Iwuanoruo Melody',
'Dedekimor Esther'
]

talk = [
'Johnson Wisdom',
'Oluwaseyi Abel',
'Ugorji Polycarp',
'Agbamu Harmony'
]


houseHolders = [
'Kupolati Ebere',
'Agbamu Patience',
'Oluwaseyi Blessing',
'Onoja Chiamaka',
'Udoh Glory Ezekiel',
'Igbiya Confidence',
'Obarah Grace',
'Iwuanoruo Melody',
'Ighavodha Doreen',
'Ubong pascaline',
'Aimiehino cecilia',
'Aimiehino augusta',
'Hoedjakou jael',
'Sarah Onyibe'
]


class myQueue():
    def __init__(self):
        self.items = []

    def addItems(self,item):
        self.items.append(item)

    def nextItem(self):
        temp = self.items.pop(0)
        self.items.append(temp)
        return temp


bible_reading_queue = myQueue()
for e in bible_reading:
    bible_reading_queue.addItems(e)

first_time_queue = myQueue()
for e in firstime:
    first_time_queue.addItems(e)

return_visit_queue = myQueue()
for e in return_visit:
    return_visit_queue.addItems(e)

bible_study_queue = myQueue()
for e in bible_study:
    bible_study_queue.addItems(e)

talk_queue = myQueue()
for e in talk:
    talk_queue.addItems(e)


house_holders_queue = myQueue()
for e in houseHolders:
    house_holders_queue.addItems(e)



def conflict(i,item, students,assistant):
    if i == 0:
        templist = students[0]+students[1]
    elif i ==len(students)-1:
        templist = assistant[i-1]+assistant+students[i]+students[i-1]
    else:
        templist = students[i-1]+assistant[i-1]+students[i]+students[i+1]

    return item in templist


for k,v in g.items():
    print(k)
    print(v)
    print()


# students = []
# for k,v in g.items():
#     if v:
#         weeks_student = []
#         for e in v:
#             if e.startswith('First Time'):
#                 weeks_student.append(first_time_queue.nextItem())
#             elif e.startswith('Return Visit'):
#                 weeks_student.append(return_visit_queue.nextItem())
#             elif e.startswith('Bible Study'):
#                 weeks_student.append(bible_study_queue.nextItem())
#         students.append(weeks_student)

# # print(students)


# partners = []

# for i in range(len(students)):
#     partners.append([])
#     while len(partners[i])<len(students[i]):
#         person = house_holders_queue.nextItem()
#         if not conflict(i,person,students,partners):
#             partners[i].append(person)
# # print(partners)


# sisters_in_program = zip(students,partners)
# # print(list(sisters_in_program))
# # print()


# sisters_weekly = {}
# n = 1
# for s,p in sisters_in_program:
#     # print(s,p)
#     sisters_weekly[n] = []
#     for i in range(len(s)):
#         sisters_weekly[n].append(s[i] + ' Assistant: ' + p[i])
#     n+=1

# import datetime

# theDate = datetime.date(2022,7,8)
# for k,v in g.items():
#     if v:
#         i = 0
#         # print(theDate)
#         str_time = datetime.datetime.strftime(theDate,'%d/%m/%y')
#         print(str_time)
#         for e in v:
#             if e.startswith('Bible Reading'):
#                 txt = e +' ' + bible_reading_queue.nextItem()
#                 print(txt)
            

#             elif e.startswith('Talk'):
#                 txt = e + ' ' + talk_queue.nextItem()
#                 print(txt)

#             else:
#                 txt = e + ' ' + sisters_weekly[k][i]
#                 print(txt)
#                 i+=1
#         theDate += datetime.timedelta(days=7)
#     print()

