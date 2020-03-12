def lesser_of_two_evens(a,b):
	'''
	Returns the lesser of two given numbers if both numbers are even,
	but returns the greater if one or both are odd
	'''
	if a%2 != 0 or b%2 !=0:
		return max(a,b)
	else:
		return min(a,b)

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

