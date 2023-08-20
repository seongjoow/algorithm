import sys
input = sys.stdin.readline

n = int(input()) # 전체 사람의 수
a, b = map(int, input().split()) # 촌수를 계산해야 하는 서로 다른 두 사람의 번호
m = int(input()) # 부모 자식 간 관계의 개수

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            cnt[i] = cnt[v] + 1
            dfs(i)

dfs(a)

if cnt[b] > 0:
    print(cnt[b])
else:
    print(-1)
