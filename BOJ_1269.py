# 대칭 차집합
# 각 집합의 원소의 개수는 200,000을 넘지 않으며, 모든 원소의 값은 100,000,000을 넘지 않는다.
# 대칭 차집합의 원소의 개수를 출력하기.
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

gyo = set(A) & set(B)
# gyo = set(A).intersection(set(B)) # 위와 동일

hap = set(A) | set(B)
# hap = set(A).union(set(B)) # 위와 동일

result = list(hap - gyo)

print(len(result))
