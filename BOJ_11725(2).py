import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if parents[i] == 0:
                queue.append(i)
                parents[i] = v


N = int(input())
graph = [[] for _ in range(N+1)]
parents = [0] * (N+1) # 내가 생각하지 못한 포인트. 별도의 visited 필요 없음.

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(1)
for i in parents[2:]:
    print(i)
