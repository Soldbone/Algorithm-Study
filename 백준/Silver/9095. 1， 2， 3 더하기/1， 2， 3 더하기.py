# 1, 2, 3 더하기

# 입력
import sys
input = sys.stdin.readline

dp = [0] * 11

# initialize
dp[1] = 1
dp[2] = 2
dp[3] = 4

# bottom-up DP w/ max()
for test in range(int(input())):
    target = int(input())
    for i in range(4, target + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[target])