# 2차원 배열의 합
# 2차원 배열에서(i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합 구하기
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N개 행, M개 열
arr = [list(map(int, input().split())) for _ in range(N)]
memo = [[0]*(M+1) for _ in range(N+1)]
K = int(input())

for i in range(1, N+1):
    for j in range(1, M+1):
        memo[i][j] = arr[i-1][j-1] + memo[i-1][j] + memo[i][j-1] - memo[i-1][j-1]

for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(memo[x][y] - memo[x][j-1] - memo[i-1][y] + memo[i-1][j-1])
