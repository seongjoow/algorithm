# 듣보잡
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 500,000 이하
a = []
b = []
c = []

for _ in range(N):
    a.append(input().rstrip())
for _ in range(M):
    b.append(input().rstrip())

# for i in a:
#     if i in b:
#         c.append(i)

c = list(set(a) & set(b))
c.sort()

print(len(c))
for i in c:
    print(i)
