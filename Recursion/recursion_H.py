def DTImplicit(toConsider, avail):

	if toConsider == [] or avail == 0:
		result = (0, ())
	elif toConsider[0][1] > avail:
		result = DTImplicit(toConsider[1:], avail)
	else:
		nextItem = toConsider[0]
		withVal, withToTake = DTImplicit(toConsider[1:], avail -nextItem[1])

		withVal += nextItem[0]
		withoutVal, withoutToTake = DTImplicit(toConsider[1:], avail)
		
		if withVal > withoutVal:
			result = (withVal, withToTake + (nextItem,))
		else:
			result = (withoutVal, withoutToTake)
	return result



stuff = [1,2,3]

print(DTImplicit(stuff,20))
