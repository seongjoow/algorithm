import sys

N = int(input()) # 운동기구의 개수
T = list(map(int, sys.stdin.readline().split())) # 각 운동기구의 근손실 정도

T.sort()

arr = []
if N%2 == 1: #개수가 홀수일 때
    for i in range(0, N//2):
        arr.append(T[i] + T[-i-2])
    arr.append(T[-1])
else: # 개수가 짝수일 때
    for i in range(0, N//2):
        arr.append(T[i] + T[-i-1])

print(max(arr))