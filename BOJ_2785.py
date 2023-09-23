# 체인
# 체인의 개수와 각각의 체인의 길이 주어짐.
# 하나의 긴 체인으로 모든 체인을 연결하기 위해 열고 닫아야 할 최소한의 고리 수.
import sys
input = sys.stdin.readline

# 체인의 개수 (2 <= N <= 500,000)
N = int(input())
# 체인의 길이 (1 <= L[i] <= 1,000,000)
for _ in range(N):
    L = list(map(int, input().split()))


