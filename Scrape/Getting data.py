import re


# pat = re.compile('\^\d [a-z]+ [a-z]+',re.IGNORECASE)

pat = re.compile('[^\d]+')

file = open(r'C:\Users\Justice\Documents\Partime student.txt')
# for e in file:
# 	print(e)

names = []
for e in file:
	for f in pat.findall(e):
		names.append(f.strip())
# for name in names:
# 	print(name)

def individuals(names):
	ind = []
	for e in names:
		if not 'PTI' in e and not '/' in e:
			ind.append(e)
		if 'PTI' in e:
			yield ' '.join(ind).strip()
			ind = []

f = individuals(names)
names_set = set()
for g in f:
	names_set.add(g)
for i in names_set:
	print(i)




# Br = r'(Bible Reading: \(\d min\.\)) (.+) \((.+)\)'
# Ic = r'(First Time: \(\d min\.\)) (.+) (\(.+\))'
# Rv = r'(Return Visit: \(\d min\.\))(.+)(\(.+\))'
# Bs = r'(Bible Study: \(\d min\.\)) (.+) (\(.+\))'
# Tl = r'(Talk: \(\d min\.\)) (.+) (\(.+\))'

# Pats = (Br, Ic, Rv,Bs,Tl)