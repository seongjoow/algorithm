# 뒤집기

import sys
input = sys.stdin.readline

S = input().rstrip()

count = {'0': 0, '1': 0}

prev = S[0]
count[prev] = 1

for i in S[1:]:
    if i != prev:
        count[i] = count[i]+1
    prev = i

print(min(count.values()))
