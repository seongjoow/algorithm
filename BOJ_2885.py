# 초콜릿 식사
# 초콜릿의 크기는 항상 2의 제곱 형태임.
# 항상 절반씩 쪼개짐.
# K개 정사각형 만들기 위해, 사야하는 가장 작은 초콜릿의 크기와 최소 몇 번 초콜릿을 쪼개야 하는지를 출력하기.

import sys
input = sys.stdin.readline

def find_size(K):
    s = 1
    while s < K:
        s = s << 1
    return s

def find_times(K, s):
    cnt = 0
    while K > 0:
        if K >= s:
            K -= s
        else:
            s //= 2
            cnt += 1
    return cnt
        
K = int(input()) # 1<=K<=1,000,000

size = find_size(K)
times = find_times(K, size)

print(size, times)

# 1
# 1 = 1
# 0

# 2
# 2 = 10
# 0

# 3 = 11
# 4 = 2+1+1
# 2

# 4
# 4 = 100
# 0

# 5 = 101
# 8 = 4+2+1+1
# 3

# 6 = 110
# 8 = 4+4 = 4+2+2
# 2

# 7 = 111
# 8 = 4+2+1+1
# 3

# 8
# 8 = 1000
# 0



