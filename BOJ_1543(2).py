# 문서 검색
# 중복되지 않게 최대 몇 번 등장하는지 출력하기.
import sys
input = sys.stdin.readline

doc = input().rstrip() # rstrip() 없으면 틀림
s = input().rstrip() # rstrip() 없으면 틀림
doc_split = doc.split(s)

print(len(doc_split) - 1)
