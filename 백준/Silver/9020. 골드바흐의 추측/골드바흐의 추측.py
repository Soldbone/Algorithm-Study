T = int(input())

nums = [int(input()) for _ in range(T)]
max_n = max(nums)

# 문제에서 주어진 n의 최댓값인 10000개를 만들어도 됨. 그러면 위의 nums와 amx()도 필요 없음
is_prime = [True] * max_n
is_prime[0] = is_prime[1] = 0

for i in range(2, int(max_n**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, max_n, i):
            is_prime[j] = False

# a + b = n
# b = n - a
# |a - b| = |2a - n|의 최솟값은 0, 그때의 a값은 n/2
for n in nums:
    a = n // 2
    while a >= 2:
        b = n - a
        if is_prime[a] and is_prime[b]:
            print(a, b)
            break
        a -= 1