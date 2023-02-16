import sys

n = int(sys.stdin.readline())
tip = []
for _ in range(n):
    tip.append(int(sys.stdin.readline()))

tip.sort(reverse=True) # 내림차순 정렬

sum = 0
for i in range(len(tip)):
    t = tip[i] - i
    if t < 0:
        break
    sum += t

print(sum)