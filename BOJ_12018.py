# Yonsei TOTO
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mileage = []
least = []
result = 0

for i in range(n):
    P, L = map(int, input().split())
    mileage.append(list(map(int, input().split())))
    mileage[i].sort(reverse = True)

    # 각 과목마다 성준이가 수강하기 위해 필요한 최소 마일리지
    if P < L:
        least.append(1)
    else:
        least.append(mileage[i][L-1])

least.sort()

for i in least:
    m = m - i
    if m < 0:
        break
    result += 1

print(result)
