# 상근이의 여행
# 다른 국가를 거쳐 가도 됨.
# 모든 국가를 여행하기 위해 타야 하는 비행기 종류의 최소 개수 출력.
# 주어지는 비행 스케줄은 항상 연결 그래프를 이룸.

import sys
input = sys.stdin.readline

T = int(input())

while(T):
    T -= 1

    N, M = map(int, input().split()) # 국가의 수 N, 비행기의 종류 M
    for _ in range(M):
        a, b = map(int, input().split())

    print(N-1)
