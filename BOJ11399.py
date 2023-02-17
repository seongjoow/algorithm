import sys

N = int(input())

p = list(map(int, sys.stdin.readline().split()))
p.sort()

time = 0
total = 0

for t in p:
    time += t
    total += time

print(total)