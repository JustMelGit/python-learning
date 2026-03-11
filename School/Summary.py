# import re

# file = open(r'C:\Users\Justice\Documents\July.txt', encoding="utf8")


# def lines(file):
# 	for line in file: yield line
# 	yield 'Bible Reading'

# def blocks(file):
# 	block = []
# 	for line in lines(file):
# 		if not line.startswith('Bible Reading'):
# 			block.append(line)
# 		elif block and line.startswith('Bible Reading'):
# 			yield ''.join(block)
# 			# yield block
# 			block = [line]
# 		# print(block)


# Br = r'Bible Reading: \(\d min\.\).+'
# Ic = r'First Time: \(\d min\.\).+'
# Rv = r'Return Visit: \(\d min\.\).+'
# Bs = r'Bible Study: \(\d min\.\).+'
# Tl = r'Talk: \(\d min\.\).+'


# Pats = (Br, Ic, Rv,Bs,Tl)

# def Search(file):
# 	m = []
# 	for block in blocks(file):
# 		for pat in Pats:
# 			if re.findall(pat,block):
# 				m.append(re.findall(pat,block)[0])
# 	return m


# def Assignment(file):
# 	week = 0
# 	meetings = {}
# 	for e in Search(file):
# 		if e.startswith('Bible Reading'):
# 			week+=1
# 			meetings['Week '+str(week)] = [e]

# 		else:
# 			meetings['Week '+str(week)].append(e)
# 	for k,v in meetings.items():
# 		for e in v:
# 			yield e	


# def Schedule(file):
# 	bibleReading = 0
# 	initialCall = 0
# 	returnVisit = 0
# 	bibleStudy = 0
# 	Talk = 0
# 	summary = ()
# 	for e in Assignment(file):
# 		e.strip()
# 		if e.startswith('Bible Reading:'):
# 			bibleReading+=1
# 			print(e)
# 		elif e.startswith('First Time:'):
# 			initialCall+=1
# 			print(e)
# 		elif e.startswith('Return Visit:'):
# 			returnVisit+=1
# 			print(e)
# 		elif e.startswith('Bible Study:'):
# 			bibleStudy+=1
# 			print(e)
# 		elif e.startswith('Talk:'):
# 			Talk+=1
# 			print(e)
# 		else: print('unknown part')

	
# 	print('bibleReading', str(bibleReading))
# 	print('init', str(initialCall))
# 	print('return', str(returnVisit))
# 	print('bible study', str(bibleStudy))
# 	print('talk',str(Talk))
# 	summary = bibleReading,initialCall,returnVisit,bibleStudy,Talk
# 	print(summary)
# 	return summary

# Meetings_may = Schedule(file)


import random

import re

file =r'C:\Users\Justice\Documents\July.txt'

def lines(file):
    f = open(file,'r',encoding='utf-8')
    for line in f: yield line
    yield 'Bible Reading'
    f.close()

def blocks(file):
    block = []
    for line in lines(file):
        if not line.startswith('Bible Reading'):
            block.append(line)
        elif block and line.startswith('Bible Reading'):
            yield block
            block = [line]



Br = r'Bible Reading: \(\d min\.\).+'
Ic = r'First Time: \(\d min\.\).+'
Rv = r'Return Visit: \(\d min\.\).+'
Bs = r'Bible Study: \(\d min\.\).+'
Tl = r'Talk: \(\d min\.\).+'

def summary(file):
    bibleReading = 0
    initialCall = 0
    returnVisit = 0
    bibleStudy = 0
    Talk = 0
    parts = ()
    for e in blocks (file):
        for f in e:
            f.strip()
            if re.match(Br,f):
                bibleReading+=1
            elif re.match(Ic,f):
                initialCall+=1
            elif re.match(Rv,f):
                returnVisit+=1
            elif re.match(Bs,f):
                bibleStudy+=1
            elif re.match(Tl,f):
                Talk+=1

    
    print('bibleReading', str(bibleReading))
    print('init', str(initialCall))
    print('return', str(returnVisit))
    print('bible study', str(bibleStudy))
    print('talk',str(Talk))
    parts = bibleReading,initialCall,returnVisit,bibleStudy,Talk
    print(parts)
    return parts

julySummary = Schedule(file)
