from itertools import groupby

a = input()
for key, group in groupby(a):
	print(tuple([len(list(group)), int(key)]), end=" ")