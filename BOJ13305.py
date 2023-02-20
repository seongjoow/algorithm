import sys

N = int(input()) # 도시의 개수
road = list(map(int, sys.stdin.readline().split())) # 도로의 길이
price = list(map(int, sys.stdin.readline().split())) # 리터당 가격

pivot = price[0]
result = 0

for i in range(len(road)):
    if pivot > price[i]:
        pivot = price[i]
    result += pivot*road[i]

print(result)