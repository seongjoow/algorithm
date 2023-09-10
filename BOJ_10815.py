# 숫자 카드
import sys
input = sys.stdin.readline

N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

check = {} # 딕셔너리

for i in n:
    check[i] = 0 # 아무 숫자로 mapping

for i in m:
    if i in check:
        print("1", end=" ")
    else:
        print("0", end=" ")
    
# 시간 초과 코드
# for i in m:
#     if i in n:
#         print("1", end=" ")
#     else:
#         print("0", end=" ")
