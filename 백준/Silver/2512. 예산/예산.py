# 예산 (복습 필요)
import sys
input = sys.stdin.readline

N = int(input())
demands = list(map(int, input().split()))
M = int(input())

start, end = 0, max(demands)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for each_budget_req in demands:
        if each_budget_req <= mid:
            sum += each_budget_req
        else:
            sum += mid
    if sum <= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)