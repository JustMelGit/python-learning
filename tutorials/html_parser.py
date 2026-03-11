file = open(r'C:\Users\Justice\Documents\May.txt')

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


k = blocks(file)
print ('<html><head><title>...</title><body>')
title = True
for block in k:
	e = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
	if title:
		print ('<h1>')
		print (block)
		print ('</h1>')
		title = False
	else:
		print ('<p>')
		print (block)
		print ('</p>')
		print ('</body></html>')





	print ('<html><head><title>...</title><body>')
	title = True
	for block in blocks(sys.stdin):
		block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
		if title:
			print ('<h1>')
			print (block)
			print ('</h1>')
			title = False
	else:
		print ('<p>')
		print (block)
		print ('</p>')
		print ('</body></html>')


class Handler:
	"""
	An object that handles method calls from the Parser.
	The Parser will call the start() and end() methods at the
	beginning of each block, with the proper block name as a
	parameter. The sub() method will be used in regular expression
	substitution. When called with a name such as 'emphasis', it will
	return a proper substitution function.
	"""
	def callback(self, prefix, name, *args):
		try:
			method = getattr(self, prefix+name, None)
			return method(*args)
		except: print('')

	def start(self, name):
		self.callback('start_', name)
	def end(self, name):
		self.callback('end_', name)
	def sub(self, name):
		def substitution(match):
			result = self.callback('sub_', name, match)
			if result is None: match.group(0)
			return result
		return substitution

class HTMLRenderer(Handler):
	"""
	A specific handler used for rendering HTML.
	The methods in HTMLRenderer are accessed from the superclass
	Handler's start(), end(), and sub() methods. They implement basic
	markup as used in HTML documents.
	"""
	def start_document(self):
		print ('<html><head><title>...</title></head><body>')
	def end_document(self):
		print ('</body></html>')
	def start_paragraph(self):
		print ('<p>')
	def end_paragraph(self):
		print ('</p>')
	def start_heading(self):
		print ('<h2>')
	def end_heading(self):
		print ('</h2>')
	def start_list(self):
		print ('<ul>')
	def end_list(self):
		print ('</ul>')
	def start_listitem(self):
		print ('<li>')
	def end_listitem(self):
		print ('</li>')
	def start_title(self):
		print ('<h1>')
	def end_title(self):
		print ('</h1>')
	def sub_emphasis(self, match):
		return '<em>%s</em>' % match.group(1)
	def sub_url(self, match):
		return '<a href="%s">%s</a>' % (match.group(1), match.group(1))
	def sub_mail(self, match):
		return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))
	def feed(self, data):
		print (data)

class Rule:
	"""
	Base class for all rules.
	"""
	def action(self, block, handler):
		handler.start(self.type)
		handler.feed(block)
		handler.end(self.type)
		return True

class HeadingRule(Rule):
	"""
	A heading is a single line that is at most 70 characters and
	that doesn't end with a colon.
	"""
	type = 'heading'
	def condition(self, block):
		return not '\n' in block and len(block) <= 70 and not block[-1] == ':'

class TitleRule(HeadingRule):
	"""
	The title is the first block in the document, provided that it is
	a heading.
	"""
	type = 'title'
	first = True
	def condition(self, block):
		if not self.first: return False
		self.first = False
		return HeadingRule.condition(self, block)


class ListItemRule(Rule):
	"""
	A list item is a paragraph that begins with a hyphen. As part of
	the formatting, the hyphen is removed.
	"""
	type = 'listitem'
	def condition(self, block):
		return block[0] == '-'
	def action(self, block, handler):
		handler.start(self.type)
		handler.feed(block[1:].strip())
		handler.end(self.type)
		return True

class ListRule(ListItemRule):
	"""
	A list begins between a block that is not a list item and a
	subsequent list item. It ends after the last consecutive list
	item.
	"""
	type = 'list'
	inside = True
	def condition(self, block):
		return True
	def action(self, block, handler):
		if not self.inside and ListItemRule.condition(self, block):
			handler.start(self.type)
			self.inside = True
		elif self.inside and not ListItemRule.condition(self, block):
			handler.end(self.type)
			self.inside = False
		return False

class ParagraphRule(Rule):
	"""
	A paragraph is simply a block that isn't covered by any of the
	other rules.
	"""
	type = 'paragraph'
	def condition(self, block):
		return True


# import sys, re
# from handlers import *
# from util import *
# from rules import *

class Parser:
	"""
	A Parser reads a text file, applying rules and controlling a
	handler.
	"""
	def __init__(self, handler):
		self.handler = handler
		self.rules = []
		self.filters = []
	def addRule(self, rule):
		self.rules.append(rule)
	def addFilter(self, pattern, name):
		def filter(block, handler):
			return re.sub(pattern, handler.sub(name), block)
		self.filters.append(filter)

	def parse(self, file):
		self.handler.start('document')
		for block in blocks(file):
			for filter in self.filters:
				block = filter(block, self.handler)
			for rule in self.rules:
				if rule.condition(block):
					last = rule.action(block, self.handler)
					if last: break
		self.handler.end('document')


class BasicTextParser(Parser):
	"""
	A specific Parser that adds rules and filters in its
	constructor.
	"""
	def __init__(self, handler):
		Parser.__init__(self, handler)
		self.addRule(ListRule())
		self.addRule(ListItemRule())
		self.addRule(TitleRule())
		self.addRule(HeadingRule())
		self.addRule(ParagraphRule())
		self.addFilter(r'\*(.+?)\*', 'emphasis')
		self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
		self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')

handler = HTMLRenderer()
parser = BasicTextParser(handler)

parser.parse(file)


# days = {'monday':[],'tueday':[], 'wednesday':[],'thurdsay':[],\
# 						'friday':[],'saturday':[],'sunday':[]}
# print(len(days))

# eng = open(r'C:\Users\Justice\Documents\Engineering.txt')
# song = open(r'C:\Users\Justice\Documents\Kingdom Songs.txt')
# pipe = open(r'C:\Users\Justice\Documents\Piping.txt')
# IstWeek = weekActivities(eng,song,pipe)



# courses = (pipe, eng)

# for e in range(len(courses)):
# 	print('courses[e]',courses[e])

# def weekActivities(file):
# 	days = {'monday':[],'tueday':[], 'wednesday':[],'thurdsay':[],\
# 						'friday':[],'saturday':[],'sunday':[]}
# 	# cour = 
# 	week = []
# 	# count=0
# 	for e in range(len(days)):
# 		f = Justice()
# 		for k in file:
# 			file[k]
# 			f.addCourse(k,file[k])
# 		print(f.dayActivities())

# import numpy



