import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split()) # 2<=N, M<=100
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip()))) # readline의 경우 맨 뒤 개행('\n')까지 입력받으므로 제거해줘야 함

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# cnt = 0

def bfs(x, y):
    queue = deque() # 큐 구현을 위해 deque 라이브러리를 사용함
    queue.append((x, y))

    # 큐가 빌 때까지 반복함
    while queue: 
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue # 반복 한 번 취소하고 다음 반복 실행
            
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 해당 노드까지의 최단 거리를 기록함
                queue.append((nx, ny))

    return graph[N-1][M-1]

result = bfs(0, 0)

print(result)
