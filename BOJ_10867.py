# 중복 빼고 정렬하기
import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
S = list(set(S))

S.sort()

for i in S:
    print(i, end=" ")
