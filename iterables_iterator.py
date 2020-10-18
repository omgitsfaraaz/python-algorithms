from itertools import combinations

n = int(input())
letters = input().split(" ")
k = int(input())

c = 0

for i in (combinations(letters, k)):
	if "a" in i:
		c = c + 1

print(c/len(list(combinations(letters, k))))