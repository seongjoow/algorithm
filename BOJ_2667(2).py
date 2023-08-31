import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # 튜플이라 괄호 한 겹 더 있음!
    graph[x][y] = 0 # 방문 처리
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and graph[nx][ny]==1:
                queue.append((nx, ny)) # 튜플이라 괄호 한 겹 더 있음!
                graph[nx][ny] = 0 # 방문 처리
                cnt += 1
    
    return cnt


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
result = []
# danji = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt = bfs(i, j)
            result.append(cnt)
            # danji += 1
            cnt = 0

result.sort()

# print(danji)
print(len(result))
for i in result:
    print(i)
