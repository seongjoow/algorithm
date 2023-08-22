import sys
input = sys.stdin.readline

N = int(input()) # 1 <= N <= 500,000
rank = []

for _ in range(N):
    rank.append(int(input()))

rank.sort()

sum = 0
for i in range(len(rank)):
    sum += abs(rank[i]-(i+1))

print(sum)
