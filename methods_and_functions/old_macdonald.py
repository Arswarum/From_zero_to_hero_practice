def old_macdonald(name):
	'''
	Function capitalizes the first and fourth letter of a name
	'''
	if len(name) > 3:
		return name[:3].capitalize() + name[3:].capitalize()
	else:
		return 'Name is too short'

print(old_macdonald('macdonald'))

