# 수리공 항승
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
leak = list(map(int, input().split()))
cnt = 0

for i in range(0, N-2):
    if leak[i+1] - leak[i] + 1 <= L:
        cnt += 1
    
