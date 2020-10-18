from itertools import product

km = list(map(int, input().split()))
k, m = km[0], km[1]
name = []
for i in range(k):
	name.append(list(map(int, input().split()))[1:])

N = list(product(*name))
ans = []
for i in N:
	s = 0
	for j in i:
		s += j ** 2
	ans.append(s % m)
print(max(ans))