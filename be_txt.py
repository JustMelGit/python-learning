# import fileinput,re

# # Matches fields enclosed in square brackets:
# field_pat = re.compile(r'\[(.+?)\]')
# # We'll collect variables in this:
# scope = {}
# # This is used in re.sub:
# def replacement(match):
# 	code = match.group(1)
# 	try:
# 	# If the field can be evaluated, return it:
# 		return str(eval(code, scope))
# 	except SyntaxError:
# 	# Otherwise, execute the assignment in the same scope...
# 		exec(code,scope)
# 	# ...and return an empty string:
# 	return ''

# print(scope)
# s = 'the sum of 2 + 8 is [2+8] '
# s1 = '[name="Mr. Gumby"]Hello, [name]'
# field_pat = re.compile(r'\[(.+?)\]')

# print(field_pat.sub(replacement,s1))





# def sublist(astring):
# 	print(astring)
# 	if len(astring) == 1:
# 		yield astring

# 	else:
# 		for i in range(len(astring)):
# 			for n in sublist(astring[0:i]+astring[i+1:]):
# 				yield [astring[i]] + n

# print(list(sublist(a)))

# a = [1,2,3]




# def flatten(nested):
# 	try:
# 		try:
# 			nested+''
# 		except TypeError:
# 			pass
# 		else:
# 			raise TypeError
# 		for sublist in nested:
# 			for element in flatten(sublist):
# 				yield element
# 	except TypeError:
# 		yield nested


# seq = list(flatten(['foo', ['bar', ['baz']]]))
# print(seq)



