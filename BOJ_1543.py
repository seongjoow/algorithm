# 문서 검색
# 중복되지 않게 최대 몇 번 등장하는지 출력하기.
import sys
input = sys.stdin.readline

doc = input().rstrip() # rstrip() 없으면 틀림
s = input().rstrip() # rstrip() 없으면 틀림
cnt = 0
i = 0

while(True):
    if i > len(doc)-len(s):
        break
    if doc[i:i+len(s)] == s:
        cnt += 1
        i += len(s)
    else:
        i += 1

print(cnt)
