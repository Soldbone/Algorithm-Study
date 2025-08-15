a = int(input())
A = sorted(map(int, input().split()), )
B = sorted(map(int, input().split()), reverse=True)
sum = 0
for i in range(a):
    sum += A[i]*B[i]
print(sum)