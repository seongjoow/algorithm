import sys

N = int(input()) # 도시의 개수
road = list(map(int, sys.stdin.readline().split())) # 도로의 길이
price = list(map(int, sys.stdin.readline().split())) # 리터당 가격

pivot = price[0]
result = 0

for i in range(1, len(price)):
    result += road[i-1]*pivot
    if pivot > price[i]:
        pivot = price[i] 

print(result)
