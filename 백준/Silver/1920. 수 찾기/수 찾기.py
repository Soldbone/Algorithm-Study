N = int(input())
A = dict.fromkeys(input().split(), 0)
M = int(input())
nums = input().split()

for word in nums:
    print(int(word in A))