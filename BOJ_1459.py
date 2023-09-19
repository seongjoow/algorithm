# 걷기
# 현재 (0, 0) -> 집 (X, Y) 최소 시간 출력하기.
# 가로나 세로로 한 블록 또는 대각선으로 이동할 수 있음.
import sys
input = sys.stdin.readline

X, Y, W, S = map(int, input().split())
# 한 블록 가는 데 걸리는 시간 W, 대각선으로 한 블록 가로지르는 시간 S
# X, Y는 10억 이하 정수, W, S는 1만 이하 자연수

# (4, 3) 5 3
# 대각선 2, 일자 3, = 6 + 15 = 21
# 대각선 2, 대각선 2, 일자 1 = 12 + 5 = 17
# 대각선 3, 일자 1 = 9 + 5 = 14

M = max(X, Y)
m = min(X, Y)
result = 0

def func():
    if X == Y:
        return min((X+Y) * W, X * S)
    
    if W < S:
        if 2 * W < S:
            return (X+Y) * W
        else:
            return (M-m)*W + m*S

    if W > S:
        # 최대한 대각선을로 많이 가기.
        return m * S + ((M-m)//2)*2*S + ((M-m)%2)*W

result = func()
print(result)
