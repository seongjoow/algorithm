# 양 한마리... 양 두마리...
# 높이 H에 걸쳐서 W개의 문자로 이루어진 문자열 하나를 입력받는다.
# 각 테스트 케이스마다, 양의 몇 개의 무리로 이루어져 있었는지를 한 줄에 출력한다.
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = '.'

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<H and 0<=ny<W and graph[nx][ny]=='#':
                queue.append((nx, ny))
                graph[nx][ny] = '.'


T = int(input())

for _ in range(T):
    H, W = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(H)]
    cnt = 0

    for x in range(H):
        for y in range(W):
            if graph[x][y] == '#':
                bfs(x, y)
                cnt += 1
    
    print(cnt)
