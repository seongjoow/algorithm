import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 위 두 줄을 아래 한 줄로 대체 가능함
    # queue = deque([(x, y)])
    graph[x][y] = 0 # 방문 처리 (별도의 visited 없이)

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx>=h or ny<0 or ny>=w:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0 # 방문 처리 (별도의 visited 없이)

            # 위 세 조건문 대신 아래 조건문으로도 가능함
            # if 0<=nx<h and 0<=ny<w and graph[nx][ny]==1:
                # queue.append((nx, ny))
                # graph[nx][ny] = 0 # 방문 처리 (별도의 visited 없이)
                

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break # 반복문 탈출

    graph = []
    result = 0

    for _ in range(h):
        graph.append(list(map(int, input().split()))) # 리스트로 입력받는 방법 알아두기

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                result += 1
    
    print(result)
