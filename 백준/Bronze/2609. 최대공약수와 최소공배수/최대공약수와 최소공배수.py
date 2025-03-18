### [ 최대공약수와 최소공배수 ] ###

# 유클리드 호제법

a, b = map(int, input().split())
AB = a * b

if b > a:
    a, b = b, a

while a % b != 0:
    a, b = b, a%b

print(b, AB//b, sep="\n")