# 양 한마리... 양 두마리...
# 높이 H에 걸쳐서 W개의 문자로 이루어진 문자열 하나를 입력받는다.
# 각 테스트 케이스마다, 양의 몇 개의 무리로 이루어져 있었는지를 한 줄에 출력한다.
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    graph[x][y] = '.'

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<H and 0<=ny<W and graph[nx][ny]=='#':
            dfs(nx, ny)


T = int(input())
result = []

while(T > 0):
    H, W = map(int, input().split()) # H는 그리드의 높이, W는 그리드의 너비
    graph = [list(input().rstrip()) for _ in range(H)]
    cnt = 0

    for x in range(H):
        for y in range(W):
            if graph[x][y] == '#':
                dfs(x, y)
                cnt += 1

    result.append(cnt)

    T -= 1

for i in result:
    print(i)
