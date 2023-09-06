# 듣보잡
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 500,000 이하
a = []
b = []
c = []

for _ in range(N):
    a.append(input().rstrip()) # rstrip() 안 하니 출력 형식이 틀림
for _ in range(M):
    b.append(input().rstrip())

# 시간 초과 코드
# for i in a:
#     if i in b:
#         c.append(i)

c = list(set(a) & set(b))
c.sort()

print(len(c))
for i in c:
    print(i)
