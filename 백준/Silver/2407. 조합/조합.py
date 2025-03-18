# 우선 입력을 받자
n, m = map(int, input().split())

# 어떻게 해결할까?
# 내가 실제로 계산할 때 사용하는 방법을 이용하자.
# e.g.) 7C3 = 7*6*5 / 3*2*1,
# 100C80 = 100C20 = 100*99*...*(100-20+1) / 20*19*18*...*1

if m > n/2:
    m = n - m

numerator = 1
for i in range(m):
    numerator *= n
    n -= 1

denominator = 1
for i in range(1, m+1):
    denominator *= i

print(numerator // denominator)