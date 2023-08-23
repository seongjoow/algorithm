import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    # 예외 처리
    if x<=-1 or x>=N or y<=-1 or y>=M: # 좌표에서 벗어날 때
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0 # 한 번 간 곳은 다시 못 가도록 변경
        for i in range(4):
            dfs(x+dx[i], y+dy[i])
        return True
    
    return False

T = int(input()) # 테스트 케이스 개수
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                cnt += 1

    print(cnt)
    