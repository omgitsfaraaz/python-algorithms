a = 'AABCAAADA'
b = ([a[i:i+3]	for i in range(0, len(a), 3)])
for i in range(len(b)):
	b[i] = set(b[i])
	print("".join(b[i]))