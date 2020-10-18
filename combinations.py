from itertools import combinations

sn = input().split()
s = sn[0]
n = int(sn[1])

for i in range(1, n+1):
	output = (list(combinations(sorted(s), i)))

	for m in output:
		print(''.join(m))
