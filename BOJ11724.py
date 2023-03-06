import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = map(int, input().split()) # 정점의 개수, 간선의 개수
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)