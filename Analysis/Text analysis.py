import random
import re


file =r"C:\Users\gnl999935\Documents\enews.txt"


def lines(file):
    f = open(file,'r',encoding='utf-8')
    for line in f: yield line
    yield '1000.0'
    f.close()

def blocks(file):
    import re
    patb =  '\d*\.0.*'
    block = []
    for line in lines(file):
        if not (re.match(patb, line)): 

                block.append(line.strip())

        elif block and (re.match(patb,line)):

                yield block
                block = [line.strip()]


for block in blocks(file):
    
    print(block)

    print()
