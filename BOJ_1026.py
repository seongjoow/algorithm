# 보물
# 작은 수는 큰 수와 곱하고, 큰 수는 작은 수와 곱해야
# 그 합이 최소가 됨

import sys
input = sys.stdin.readline

N = int(input()) # 0 < N <= 50
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = 0

B.sort() # sort()는 리스트 본체를 정렬함
A.sort(reverse=True)

for i in range(N):
    result += A[i]*B[i]

print(result)
