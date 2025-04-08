# 1로 만들기 (복습 필요)
import sys

n = int(sys.stdin.readline())
dp = [0] * (10**6 + 1)

for i in range(2, n+1):
    # 2나 3으로 나눠지지 않으면 1을 빼는 연산이 수행되어 count++
    # 즉, 업데이트된 dp[i]는 1을 빼는 경우를 의미함.
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1) # 1을 빼는 경우 vs. 2로 나눈 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1) # 1을 빼는 경우 vs. 3으로 나눈 경우

print(dp[n])
