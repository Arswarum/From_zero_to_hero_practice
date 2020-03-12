def animal_crackers(text):
	'''
	Takes two-word string and returns True if both words begin with
	same later
	'''
	return text.split()[0][0] == text.split()[1][0]

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
