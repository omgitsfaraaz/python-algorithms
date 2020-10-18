from itertools import combinations_with_replacement

sn = input().split()
s = sn[0]
n = int(sn[1])
output = list(combinations_with_replacement(sorted(s), n))
for i in output:
	print(''.join(i))
