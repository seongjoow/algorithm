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

# 사람 순서의 모든 경우의 수에 따른 비교? X
# (주려고 했던 돈) - (0, 1, 2, 3, ...) 의 합
# 단, 팁이 음수면 0으로 계산.
# 왜 내림차순 정렬한 게 가장 큰 팁의 합을 보장해 주는 건지 이해가 안 간다.