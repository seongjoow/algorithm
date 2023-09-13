# 영역 구하기
# 직사각형 내부를 제외한 부분이 몇 개의 분리된 영역으로 나누어지는지,
# 분리된 각 영역의 넓이가 얼마인지 (오름차순, 빈칸 두고) 출력

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    graph[x][y] = 1
    global cnt
    cnt += 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<M and 0<=ny<N and graph[nx][ny]==0:
            dfs(nx, ny)
            

M, N, K = map(int, input().split()) # 100 이하 자연수 # M: y좌표(행 개수), N: x좌표(열 개수)
graph = [[0 for _ in range(N)] for _ in range(M)] # 몰랐던 초기화 방법
cnt = 0
area = []

# 직사각형 내부를 1로 표시
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
    # 0, 2, 4, 4 입력시, 직사각형 내부는 아래와 같음
    # (0, 2) (1, 2) (2, 2) (3, 2)
    # (0, 3) (1, 3) (2, 3) (3, 3)

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            dfs(i, j)
            area.append(cnt)
            cnt = 0

area.sort()

print(len(area))
for i in area:
    print(i, end=" ")
