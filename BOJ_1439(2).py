# 뒤집기
# S, 변화 횟수(cnt), 답
# 0, 1, 0
# 01, 2, 1
# 010, 3, 1
# 0101, 4, 2
# 01010, 5, 2

import sys
input = sys.stdin.readline

S = input().rstrip() # rstrip() 없으면 틀림.
prev = '?'
cnt = 0

for i in S:
    if i != prev:
        cnt += 1
        prev = i

print(cnt//2) # 몫
