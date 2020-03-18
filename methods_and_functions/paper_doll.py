def paper_doll(text):
	ans=''
	for letter in text:
		ans += (letter*3)
	return ans

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))
