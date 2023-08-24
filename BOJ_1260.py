import sys
from collections import deque
input = sys.stdin.readline

def dfs(v):
    # 방문 처리
    visited[v] = 1
    print(v, end=" ")

    for i in graph[v]:
        if visited[i] == 0: # if not visited[i]:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)

    visited[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1


# 정점의 개수 N, 간선의 개수 M, 탐색 시작할 정점의 번호 V (1 <= N, M <= 1000)
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)] # N이 아닌 N+1이라는 점 기억하기

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 정렬
for i in graph:
    i.sort()

visited = [0] * (N+1)
dfs(V)
print()

visited = [0] * (N+1)
bfs(V)
