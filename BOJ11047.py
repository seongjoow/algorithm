import sys

n, k = map(int, sys.stdin.readline().split())

value = [int(sys.stdin.readline()) for _ in range(n)]
value.reverse()

result = 0
for val in value:
    if k >= val:
        num = k//val
        k -= val*num
        result += num

print(result)