# 수리공 항승
import sys
input = sys.stdin.readline

N, L = map(int, input().split()) # 물 새는 곳의 개수 N, 테이프 길이 L (1,000 이하 자연수)
leak = list(map(int, input().split())) # 물 새는 곳의 위치 (1,000 이하 자연수)
cnt = 0

for i in range(0, N-2):
    if leak[i+1] - leak[i] + 1 <= L:
        cnt += 1
    
