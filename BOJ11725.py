import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input()) # 노드의 개수
graph = [[] for _ in range(N+1)]
parents = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    for i in graph[v]:
        if parents[i] == 0:
            parents[i] = v
            dfs(i)

dfs(1)

for i in range(2, N+1):
    print(parents[i])