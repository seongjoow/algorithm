# Oil Deposits
# n 글자의 m 줄을 입력 받는다.
# '*'는 기름 없음, '@'는 기름 있음을 나타낸다.
# 가로, 세로, 대각선으로 인접하면 같은 oil deposit이다.
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def dfs(x, y):
    graph[x][y] = '*' # 방문 처리

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<m and 0<=ny<n and graph[nx][ny]=='@':
            dfs(nx, ny)


while True:
    m, n = map(int, input().split())
    if m == 0:
        break

    graph = [list(input().rstrip()) for _ in range(m)]
    cnt = 0

    for x in range(m):
        for y in range(n):
            if graph[x][y] == '@':
                dfs(x, y)
                cnt += 1
    
    print(cnt)
    