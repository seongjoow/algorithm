# 행렬 곱셈
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

C = [[0 for _ in range(K)] for _ in range(N)] # 2차원 배열 초기화

for n in range(N):
    for k in range(K):
        for m in range(M): # 내가 생각 못 해낸 부분 (여기 두 줄)
            C[n][k] += A[n][m] * B[m][k]

for i in range(N):
    for j in range(K):
        print(C[i][j], end=' ')
    print()
