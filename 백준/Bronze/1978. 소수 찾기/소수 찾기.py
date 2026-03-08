def is_prime(n: int) -> bool:
    if n < 2:
        return False

    if n % 2 == 0:
        return n == 2

    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


N = int(input())
nums = list(map(int, input().split()))
count = 0
for n in nums:
    if is_prime(n):
        count += 1

print(count)
