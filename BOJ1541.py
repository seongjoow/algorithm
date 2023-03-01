arr = input().split('-')

result = 0
for i, val in enumerate(arr):
    if i == 0:
        for p in val.split('+'):
            result += int(p)
    else:
        for p in val.split('+'):
            result -= int(p)

print(result)