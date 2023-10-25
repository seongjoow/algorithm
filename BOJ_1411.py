# 비슷한 단어
# 서로 다른 알파벳은 같은 알파벳으로 바꿀 수 없음. 
# 단어가 여러 개 주어졌을 때, 몇 개의 쌍이 비슷한지 출력하기
import sys
input = sys.stdin.readline

N = int(input())
li = [input().rstrip() for _ in range(N)]
# 위 한 줄과 동일
# li = []
# for _ in range(N):
#     li.append(input().rstrip())

cnt = 0

# for word in li:
for i in range(N-1): # N 아님 주의.
    for j in range(i+1, N):
        word1 = li[i]
        word2 = li[j]

        flag = True
        check1 = [0] * 26
        check2 = [0] * 26
        for k in range(len(word1)):
            idx1 = ord(word1[k]) - ord('a')
            idx2 = ord(word2[k]) - ord('a')
            
            if check1[idx1] == 0 and check2[idx2] == 0:
                check1[idx1] = word2[k]
                check2[idx2] = word1[k]
            elif check1[idx1] != word2[k]:
                flag = False
                break
        if flag:
            cnt += 1

print(cnt)
