from collections import Counter

n = int(input())
stock = list(map(int, input().split(' ')))
customers = int(input())
Dict = Counter(stock)

p = 0

for i in range(customers):
    size, price = map(int, input().split(' '))

    if Dict[size]:
        Dict[size] -= 1
        p = p + price

print(p)