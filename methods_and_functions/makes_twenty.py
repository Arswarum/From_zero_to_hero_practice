def makes_twenty(n1,n2):
	'''
	INPUT: two integers
	RETURN: True if the sum of integers is 20 or if one of the integer is 20
	if not return False.
	'''
	return n1 + n2 == 20 or n1 == 20 or n2 == 20

print(makes_twenty(20,10))
print(makes_twenty(2,3))
print(makes_twenty(13,7))
