import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
result = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i)
        result += 1

print(result)
