def summer_69(arr):
	arr2 =[]
	button = True
	for num in arr:
		if num == 6:
			button = False

		if num == 9:
			button = True
			continue
		if button:
			arr2.append(num)

	return sum(arr2)

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
