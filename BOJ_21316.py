# 스피카
# 12개의 별(1~12)을 12개의 선분으로 이음.
# 스피카는 몇 번 별인지 출력하기. (정수 하나 출력)

# subgraph 구조로 스피카 노드 특정하기.
# 1. 인접한 노드(연결된 간선)가 3개이면서
# 2. 인접 노드의 간선이 6개(1+2+3)
import sys
input = sys.stdin.readline

graph = [[] for _ in range(13)]

for _ in range(12):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, 13):
    if len(graph[i]) == 3:
        sum = 0
        for j in graph[i]:
            sum += len(graph[j])
        
        if sum == 6:
            print(i) # 문제에서 무엇을 출력하라고 했는지 제대로 보자!
            break
