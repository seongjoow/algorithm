import sys
input = sys.stdin.readline

n = int(input()) # 2 <= n <= 500
m = int(input()) # 1 <= m <= 10000

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
result = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited[1] = 1

for i in graph[1]:
    visited[i] = 1
    result += 1

for i in graph[1]:
    for j in graph[i]:
        if visited[j] == 0:
            visited[j] = 1
            result += 1

print(result)
