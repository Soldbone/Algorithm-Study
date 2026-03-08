n = int(input())
count = 0
lst = list(map(int, input().split()))
for x in lst:
    for i in range(2, x):
        if x % i == 0:
            count -= 1
            break
    count += 1
if 1 in lst:
    count -= 1
print(count)