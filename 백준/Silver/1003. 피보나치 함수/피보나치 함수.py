# 피보나치 함수 - DP

dp = [0] * 1001
print_count = [0] * 1001
print_count[0] = (1, 0)
print_count[1] = (0, 1)

def fibonacci(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    
    if dp[n] != 0:
        return dp[n]

    dp[n] = fibonacci(n-1) + fibonacci(n-2)
    zero_count1, one_count1 = print_count[n-1]
    zero_count2, one_count2 = print_count[n-2]
    print_count[n] = (zero_count1+zero_count2, one_count1+one_count2)
    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    fibonacci(n)
    print(*print_count[n])