def lines(file,bou_str='\n'):
	f = open(file,'r',encoding='utf-8')
	for line in f:
		yield line
	yield bou_str
	f.close()

def blocks(file,bou_str):
	block = []
	for line in lines(file,bou_str):
		if not line.startswith(bou_str):
			block.append(line)
		elif block and line.startswith(bou_str):
			block.append(line)
			yield ''.join(block)
			block = []