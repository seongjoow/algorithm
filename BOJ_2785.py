# 체인
# 체인의 개수와 각각의 체인의 길이 주어짐.
# 하나의 긴 체인으로 모든 체인을 연결하기 위해 열고 닫아야 할 최소한의 고리 수.
import sys
input = sys.stdin.readline

# 체인의 개수 (2 <= N <= 500,000)
N = int(input())
# 체인의 길이 (1 <= L[i] <= 1,000,000)
L = list(map(int, input().split()))

# 아이디어: 가장 짧은 체인부터 소모해가며 체인들을 연결.
chains_to_connect = N
chains_connected = 1

L.sort()
for chain in L:
    if chains_connected + chain >= chains_to_connect:
        break
    else:
        chains_connected += chain
        chains_to_connect -= 1

print(chains_to_connect - 1)
