import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    # 방문 처리
    graph[x][y] = 0

    global cnt # 생각 못 했던 부분. 몰랐던 개념.
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<N and graph[nx][ny]==1:
            dfs(nx, ny)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input()) # 지도의 크기 (5<=N<=25)

graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))
# 위 3줄을 아래 한 줄로 대체 가능함
# graph = [list(map(int, input().rstrip())) for _ in range(N)]

danji = 0 # 총 단지 수
result = [] # 단지 내 집의 수

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            result.append(cnt)
            danji += 1

result.sort()
print(danji)
for i in result:
    print(i)
