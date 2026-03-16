a, b, c = map(int, input().split())

result = 1
num = a % c
n = b

while n > 0:
    if n % 2 == 1:
        result = (result * num) % c
    num = (num * num) % c
    n //= 2

print(result)