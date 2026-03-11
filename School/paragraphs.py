import sys
sys.path.append(r'C:\Users\HP\Documents\Python_new\Utilities')  # full folder path
from util import blocks

import re
file1 = r'C:\Users\HP\Documents\sep-oct 2025.txt'
bl = blocks(file1,'Wetin We Don Learn? (3 min.)')
pat = r'^\d+\.\s*[?\w""\s—,!-]+ \(\d+ min\.\)'

for e in bl:
	mat = re.findall(pat,e,re.M)
	for items in mat:
		print(items)
	print()
	print('new week '*5)
	print()
	