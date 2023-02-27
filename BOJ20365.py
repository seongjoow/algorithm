N = int(input())
arr = input()

result = 1
for i in range(N):
    if arr[i] == arr[0]:
        tmp = arr[0]
        continue
    if arr[i] != tmp:
        tmp = arr[i]
        result += 1

print(result)