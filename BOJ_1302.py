# 베스트셀러
import sys
input = sys.stdin.readline

N = int(input()) # 1,000 이하 자연수
titles = {}

for _ in range(N):
    t = input().rstrip()

    if t in titles: # if t in titles.keys(): 과 동일
        titles[t] += 1
    else:
        titles[t] = 1

max_keys = [k for k, v in titles.items() if v == max(titles.values())]

max_keys.sort()

print(max_keys[0])
