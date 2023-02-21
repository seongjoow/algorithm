import sys

N = int(input())
drinks = list(map(int, sys.stdin.readline().split()))

drinks.sort(reverse=True) # 오름차순 정렬

result = drinks[0]
for i in range(1, N):
    result += drinks[i]/2

print(result)