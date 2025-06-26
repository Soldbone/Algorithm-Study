# 가장 긴 증가하는 부분 수열
# 복습이 필요하다. 코드는 단순한데 아이디어를 떠올리지 못했다.

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
