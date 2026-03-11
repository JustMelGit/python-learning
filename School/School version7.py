import sys
sys.path.append(r'C:\Users\HP\Documents\Python_new\Utilities')
from util import blocks

import re
file1 = r'C:\Users\HP\Documents\sep-oct 2025.txt'
bl = list(blocks(file1,'Wetin We Don Learn? (3 min.)'))
pat = r'^\d+\.\s*[?\w""\s—,!-]+ \(\d+ min\.\)'

g = {}
for k,v in enumerate(bl,1):
    mat = re.findall(pat,v,re.M)
    g[k] = mat

print(g)

                       
bible_reading = [
'Ekanem James',
'Samuel Prince',
'Oriki Israel',
'Ugorji Polycarp',
'Agbamu Harrison',
'Agbamu Harmony',
'Barak Anderson',
'Rotimi Abanikanda',
# 'Eze Enoch',
# 'Inyang Jephtha',
]



de_start_discussion = [
'Ighavodha Amber',
'Agbamu Hananiel',
'Abel Hope',
'Ighavodha Annabel',
'Edamrere Favour',
'Ighavodha Adele',
# 'Obarah Grace',
# 'Amuta Blessing',
'Amuta Comfort',
# 'Anthony Queen',
# 'Igbinoba Unity',
# 'Kupolati Ebere',
'Nwachukwu Grace',
'Onwumeni Shulamite',
# 'Yombo Omabowale', 
'Ekanem Stella',
'Ighavodha Doreen',
'Iwuanoruo Melody',
'Odemo Mercy',
'Ogundoro Favour',
'Osuoha Joy',
'Agbamu Patience'
]

de_check_the_person_again = [
'Agbamu Patience',
'Edamrere Favour',
# 'Obarah Grace',
# 'Amuta Blessing',
'Amuta Comfort',
# 'Anthony Queen',
# 'Igbinoba Unity',
# 'Kupolati Ebere',
# 'Nwachukwu Grace',
'Abel Hope',
# 'Onwumeni Shulamite',
# 'Yombo Omabowale', 
'Ekanem Stella',
# 'Ighavodha Doreen',
'Iwuanoruo Melody',
# 'Odemo Mercy',
# 'Ogundoro Favour',
'Osuoha Joy'
]


de_make_disciples =[
'Obarah Grace',
# 'Amuta Blessing',
# 'Amuta Comfort',
# 'Anthony Queen',
# 'Dedekimor Esther',
# 'Eze Enoch',
'Igbinoba Unity',
# 'Inyang Jephtha',
# 'Kupolati Ebere',
# 'Nwachukwu Grace',
# 'Nwachukwu Joshua',
# 'Onwumeni Shulamite',
# 'Yombo Abiodun',
'Yombo Omabowale' 
]


wetin_you_believe =[
# 'Amuta Blessing',
# 'Amuta Comfort',
'Anthony Queen',
# 'Dedekimor Esther',
# 'Eze Enoch',
# 'Igbinoba Unity',
# 'Inyang Jephtha',
# 'Kupolati Ebere',
# 'Kupolati Omoniyi',
# 'Nwachukwu Grace',
# 'Nwachukwu Joshua',
'Onwumeni Shulamite',
# 'Yombo Omabowale', 
]



talk = [
# 'Agbamu Harmony',
# 'Barak Anderson',
# 'Johnson Wisdom',
'Ugorji Polycarp',
# 'Inyang Jephtha',
# 'Ekanem James',
'Rotimi Abanikanda',
# 'Rotimi Eniafe',
]


house_holders = [
'Abel Hope',
'Agbamu Patience',
'Edamrere Favour',
'Obarah Grace',
'Amuta Blessing',
'Amuta Comfort',
'Anthony Queen',
'Igbinoba Unity',
'Kupolati Ebere',
'Nwachukwu Grace',
'Onwumeni Shulamite',
'Yombo Omabowale', 
'Ekanem Stella',
'Ighavodha Doreen',
'Iwuanoruo Melody',
'Odemo Mercy',
'Ogundoro Favour',
'Osuoha Joy'
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

de_start_discussion_queue = myQueue()
for e in de_start_discussion:
    de_start_discussion_queue.addItems(e)

de_check_the_person_again_queue = myQueue()
for e in de_check_the_person_again:
    de_check_the_person_again_queue.addItems(e)

de_make_disciples_queue = myQueue()
for e in de_make_disciples:
    de_make_disciples_queue.addItems(e)

wetin_you_believe_queue = myQueue()
for e in wetin_you_believe:
    wetin_you_believe_queue.addItems(e)

talk_queue = myQueue()
for e in talk:
    talk_queue.addItems(e)


house_holders_queue = myQueue()
for e in house_holders:
    house_holders_queue.addItems(e)



def conflict(i,item, students,assistant):
    if i == 0:
        templist = students[0]+students[1]
    elif i ==len(students)-1:
        templist = assistant[i-1]+assistant+students[i]+students[i-1]
    else:
        templist = students[i-1]+assistant[i-1]+students[i]+students[i+1]

    return item in templist




students = []
for k,v in g.items():
    if v:
        weeks_student = []
        for e in v:
            if 'De Start Discussion' in e:
                weeks_student.append(de_start_discussion_queue.nextItem())
            elif 'De Check the Person Again' in e:
                weeks_student.append(de_check_the_person_again_queue.nextItem())
            elif 'De Make Disciples' in e:
                weeks_student.append(de_make_disciples_queue.nextItem())
            elif 'Wetin You Believe' in e:
                weeks_student.append(wetin_you_believe_queue.nextItem())
        students.append(weeks_student)

print(students)


partners = []

for i in range(len(students)):
    partners.append([])
    while len(partners[i])<len(students[i]):
        person = house_holders_queue.nextItem()
        if not conflict(i,person,students,partners):
            partners[i].append(person)
print(partners)


sisters_in_program = zip(students,partners)


sisters_weekly = {}
n = 1
for s,p in sisters_in_program:
    # print(s,p)
    sisters_weekly[n] = []
    for i in range(len(s)):
        sisters_weekly[n].append(s[i] + ' Assistant: ' + p[i])
    n+=1

print(sisters_weekly)

import datetime

theDate = datetime.date(2025,9,5)
for k,v in g.items():
    if v:
        i = 0
        # print(theDate)
        str_time = datetime.datetime.strftime(theDate,'%d/%m/%y')
        print(str_time)
        for e in v:
            if 'Bible Reading' in e:
                txt = e +' ' + bible_reading_queue.nextItem()
                print(txt)
            

            elif 'Talk' in e:
                txt = e + ' ' + talk_queue.nextItem()
                print(txt)

            elif 'De Make Disciples' in e or 'De Start Discussion' in e or 'De Check the Person Again' in e or 'Wetin You Believe' in e:
                txt = e + ' ' + sisters_weekly[k][i]
                print(txt)
                i+=1
            else:
                print(e)
        theDate += datetime.timedelta(days=7)
    print()

