A, B = map(int, input().split())

cnt = 0
while A != B:
    if A > B:
        cnt = -2
        break
    elif B%2 == 0:
        B = B//2
        cnt += 1
    elif B%10 == 1:
        B = B//10
        cnt += 1
    else:
        cnt = -2
        break

print(cnt+1)