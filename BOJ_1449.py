# 수리공 항승
import sys
input = sys.stdin.readline

N, L = map(int, input().split()) # 물 새는 곳의 개수 N, 테이프 길이 L (1,000 이하 자연수)
leak = list(map(int, input().split())) # 물 새는 곳의 위치 (1,000 이하 자연수)
leak.sort()

cnt = 1
left = leak[0] - 0.5 # 테이프 시작 위치

for i in range(N):
    # break문을 넣으려다가 계속 틀렸음. break문 필요 없음.
    if left <= leak[i] <= left + L:
        continue
    
    # 테이프를 새로 붙임.
    left = leak[i] - 0.5
    cnt += 1

print(cnt)
