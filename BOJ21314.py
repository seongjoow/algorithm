string = input()
max = ''
min = ''

cnt = 0
for s in string:
    if s == 'M':
        cnt += 1 # 연속되는 M의 개수
    else: # s == 'K'
        if cnt: # 앞에 M이 없는 경우
            max += str(10**cnt*5)
            min += str(10**cnt+5)
        else: # 앞에 M이 붙어있는 경우
            max += '5'
            min += '5'
        cnt = 0

if cnt: # 문자열이 M으로 끝나는 경우
    max += '1'*cnt
    min += str(10**(cnt-1))

print(max)
print(min)