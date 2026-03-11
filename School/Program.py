import re
file = open(r'C:\Users\HP\Documents\july-august.txt', encoding="utf8")
def lines(file):
    for line in file: yield line
    yield 'Bible Reading'

def blocks(file):
    block = []
    for line in lines(file):
        if not line.startswith('Bible Reading'):
            block.append(line)
        elif block and line.startswith('Bible Reading'):
            yield ''.join(block)
            # yield block
            block = [line]


Br = r'(Bible Reading: \(\d min\.\)) (.+) \((.+)\)'
Ic = r'(Initial Call: \(\d min\.\)) (.+) \((.+)\)'
Rv = r'(Return Visit: \(\d min\.\))(.+)\((.+)\)'
Bs = r'(Bible Study: \(\d min\.\)) (.+) \((.+)\)'
Tl = r'(Talk: \(\d min\.\)) (.+) \((.+)\)'

Pats = (Br, Ic, Rv,Bs,Tl)

def Search(file):
    m = []
    for block in blocks(file):
        for pat in Pats:
            if re.findall(pat,block):
                m.append(re.findall(pat,block))
    return m


def Assignment(file):
    week = 0
    Meetings = {}
    for e in Search(file):
        if e[0][0].startswith('Bible Reading'):
            week+=1
            Meetings['Week'+str(week)] = [e]
        else:
            Meetings['Week'+str(week)].append(e)
    return (Meetings)



def Month(file):
    MeetingParts = Assignment(file)
    for k in MeetingParts:
        for e in (MeetingParts[k]):
            for f in e:
                yield f



class student(object):
    def __init__(self, name):
        self.name = name
        self.spechQualities = []
        self.Assignment = []

    def Assignment(self, Date, spechQuality):
        self.spechQualities.append(spechQuality)
        self.Assignment.append(Date)

    def getAssignment(self):
        for e in self.Assignment:
            print(e)
    # def getS

    def __str__(self):
        return self.name.title()

class yBrother(student):
    pass

class ySister(student):
    pass

class mSister(student):
    pass

class mBrother(student):
    pass

class sStudy(student):
    pass



class school(object):
    def __init__(self, summary):
        self.summary = summary
        self.yBrothers = []
        self.mBrothers = []
        self.mSisters = []
        self.sStudys = []
        self.ySisters = []

    def Addstudent(self,list):
        for e in list:
            if isinstance(e,yBrother):
                self.yBrothers.append(e)
            elif isinstance(e,mBrother):
                self.mBrothers.append(e)
            elif isinstance(e,ySister):
                self.ySisters.append(e)
            elif isinstance(e,mSister):
                self.mSisters.append(e)
            else:
                self.sStudys.append(e)

    def nextReader(self):
        List = self.yBrothers[:]
        for i in range(self.summary[0]):
            temp = List.pop(0)
            List.append(temp)
            yield temp

    def nextInitial(self):
        List = self.ySisters[:]
        for i in range(self.summary[1]):
            temp = List.pop(0)
            List.append(temp)
            yield temp

    def nextReturn(self):
        List = self.mSisters[:]
        for i in range(self.summary[2]):
            temp = List.pop(0)
            List.append(temp)
            yield temp

    def nextStudy(self):
        List = self.sStudys[:]
        for i in range(self.summary[3]):
            temp = List.pop(0)
            List.append(temp)
            yield temp

    def nextTalk(self):
        List = self.mBrothers[:]
        for i in range(self.summary[4]):
            temp = List.pop(0)
            List.append(temp)
            yield temp



HAM = yBrother('AGBAMU HARMONY')
AND = yBrother('BARAK ANDRESON')
JOH = yBrother('MAINA JOHN')
TEF = yBrother('OGHENETEJIRI TEFA')
FRI = yBrother('ONOJA FRIDAY')
ISR = yBrother('ORIKI ISRAEL')
JOE = yBrother('SMART JOEGODSON')

PAT = mSister('AGBAMU PATIENCE')
EBE = mSister('AMAEFULA EBERECHI')
EST = mSister('DEDEKIMOR ESTHER')
MEL = mSister('IWUANORUO MELODY')
PRI = mSister('MBA PRISCILLA')
LOV = mSister('OKON LOVE')
BLE = mSister('OLUWASEYI BLESSING')
CHI = mSister('ONOJA CHIAMAKA')
OJO = mSister('ONOJA OJOMA')
EZE = mSister('UDOH GLORY EZEKIEL')


CON = sStudy('IGBIYA CONFIDENCE')
DOR = sStudy('IGHAVODHA DOREEN')
GRA = sStudy('OBARAH GRACE')
END = sStudy('KUPOLATI EBERE')


KIN = mBrother('AMAEFULA KINGSLEY')
WIS = mBrother('JOHNSON WISDOM')
ABE = mBrother('OLUWASEYI ABEL')
POL = mBrother('UGORJI POLYCARP')

HAR = ySister('AGBAMU HARVEST')
HAV = ySister('AGBAMU HAVILAH')
AMB = ySister('IGHAVODHA AMBER')
ANN = ySister('IGHAVODHA ANNABEL')

student_usernames = [TEF,
FRI,
ISR,
JOE,
HAM,
AND,
JOH,

PAT,
EBE,
EST,
MEL,
CON,
DOR,
END,
PRI,
GRA,
LOV,
BLE,
CHI,
OJO,
EZE,
KIN,
WIS,
ABE,
POL,
HAR,
HAV,
AMB,
ANN]


# CMS = school()
# CMS.Addstudent(student_usernames)


TMS = school((9, 5, 7, 4, 4))
TMS.Addstudent(student_usernames)



# print(CMS.Biblereaders)
# [print(e) for e in TMS.nextReader()]




# def Schedule(file):
#     for e in Month(file):
#         print(e[0],e[1].strip(),e[2])

# Meetings_may = Schedule(file)

def assignParts(school, file):
    Weeks = 0
    Init = 0
    Reading = 0
    Retu = 0
    bStu = 0
    Tal = 0
    Readers = list(school.nextReader())
    Initial = list(school.nextInitial())
    Return = list(school.nextReturn())
    Study = list(school.nextStudy())
    Talk = list(school.nextTalk())
    
    weeklyHouseholders = {}

    for e in Month(file):
        if e[0].startswith('Bible Re'):
            Weeks+=1
            # print>>f('Week '+str(Weeks))
            print(e[0], Readers[Weeks-1])

        elif e[0].startswith('Initial Ca'):
            print(e[0], Initial[Init])
            Init+=1

        elif e[0].startswith('Return Vis'):
            print(e[0], Return[Retu])
            Retu+=1

        elif e[0].startswith('Bible Stu'):
            print(e[0], Study[bStu])
            bStu+=1

        else:
            print(e[0], Talk[Tal])
            Tal+=1
    print(weeklyHouseholders)
    print(houseHolders)


# with open(r'C:\Users\Justice\OneDrive\Documents\meetings2.txt', 'w') as file_output:
# f = open(r'C:\Users\Justice\Desktop\Kingdom Songs.txt','w')
assignParts(TMS, file)
# # print(k)

# pat ='Return Visit: (3 min.) () 
# Return Visit: (3 min.) Agbamu Patience  Use the sample conversation.  Study 6
