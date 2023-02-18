import sys

n = int(input())
prices = [int(sys.stdin.readline()) for _ in range(n)]

prices.sort(reverse=True)

result = 0
for i, price in enumerate(prices):
    if i%3 == 2:
        continue
    result += price

print(result)