import re
def lines(file):
    for line in file: yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []

def Search(file):
    found = []
    for block in blocks(file):
        for pat in Pats:
            if re.findall(pat,block):
            	m = re.findall(pat,block)
            	found.append(m)
    return found

out = r'No\..+TO BE COVERED.+MINUTES'
Br = r'(Bible Reading: \(\d min\.\)) (.+) \((.+)\)'
Ic = r'(Initial Call: \(\d min\.\)) (.+) \((.+)\)'
Rv = r'(Return Visit: \(\d min\.\))(.+)\((.+)\)'
Bs = r'(Bible Study: \(\d min\.\)) (.+) \((.+)\)'
Tl = r'(Talk: \(\d min\.\)) (.+) \((.+)\)'


file = open(r'C:\Users\Justice\OneDrive\Documents\Publictalks.txt', encoding="utf8")
Pats = [out]
results = Search(file)
print(results)