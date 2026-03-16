import sys

input = sys.stdin.readline
candidate = set()
nums = []
N = int(input())
for _ in range(N):
    nums.append(int(input()))

nums.sort()
for i in range(N):
    for j in range(i, N):
        candidate.add(nums[i] + nums[j])

BREAK_NESTED_FOR = False
for i in range(N - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        if nums[i] - nums[j] in candidate:
            print(nums[i])
            BREAK_NESTED_FOR = True
            break
    if BREAK_NESTED_FOR:
        break
