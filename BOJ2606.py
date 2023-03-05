import sys
input = sys.stdin.readline

v = int(input()) # 컴퓨터의 수
e = int(input()) # 직접 연결된 컴퓨터 쌍의 수
graph = [[] for _ in range(v+1)]
visited = [0] * (v+1)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = 1
    for node in graph[v]:
        if visited[node] == 0:
            dfs(node)

dfs(1)
print(sum(visited) - 1)