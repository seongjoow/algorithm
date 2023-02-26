import sys

N = int(input()) # 운동기구의 개수
T = list(map(int, sys.stdin.readline().split())) # 각 운동기구의 근손실 정도

T.sort()

arr = []
if N%2 == 1:
    m = T.pop(-1)
    arr.append(m)
for i in range(len(T)//2):
	arr.append(T[i] + T[-i-1])
    
print(max(arr))