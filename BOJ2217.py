import sys

n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(sys.stdin.readline()))

ropes.sort()

# (수용무게) * (수용무게가 크거나 같은 로프의 개수) 중 최댓값
capacity = []
for i in ropes:
    capacity.append(i*n)
    n -= 1

print(max(capacity))