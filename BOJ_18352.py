# 1~N 텔레포트 정거장
# X에서 X+1 또는 X-1 또는 연결된 지점으로 이동 가능, 각 1초 소요
# N과 텔레포트 연결 정보 주어질 때, # S -> E 최소 시간

import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    queue = deque()
    queue.append((v, 0))

    while queue:
        X, cnt = queue.popleft()
        if X == E:
            return cnt
        if 1 <= X <= N:
            if visited[X] == 0:
                visited[X] = 1
                queue.append((X+1, cnt+1))
                queue.append((X-1, cnt+1))
                if len(graph[X]) > 0:
                    for i in graph[X]:
                        queue.append((i, cnt+1))
                

N, M = map(int, input().split())
S, E = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


print(bfs(S))
