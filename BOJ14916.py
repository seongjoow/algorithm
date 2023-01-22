import sys

n = int(sys.stdin.readline())

num = 0

# 5원짜리 개수를 최대로 거슬러 줄 수 있을 때
if ( (n%5)%2 == 0 ):
    num = n//5 + (n%5)//2
# 5원짜리 개수를 하나 줄여서 거슬러 줄 수 있을 때
elif ( (n%5 + 5) %2 == 0 ):
    if ( n>=5 ):
        num = n//5 - 1 + (n%5 + 5)//2
    else:
        num = -1
# 거슬러 줄 수 없으면 -1
else:
    num = -1

print(num)
