# 치킨 TOP N
import sys
input = sys.stdin.readline

N = int(input())
chicken_lst = list(map(int, input().split()))
k = int(input())

num_of_group = N // k

result = []
for i in range(num_of_group, len(chicken_lst)+1, num_of_group):
    result.extend(sorted(chicken_lst[i-num_of_group:i]))
#     print(f"i: {result}")

# print()
print(*result)


