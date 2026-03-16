import sys

input = sys.stdin.readline
left = list(input().rstrip())
right = []
M = int(input())
for _ in range(M):
    command = input().split()
    match command[0]:
        case "L":
            if left:
                right.append(left.pop())
        case "D":
            if right:
                left.append(right.pop())
        case "B":
            if left:
                left.pop()
        case "P":
            left.append(command[1])
print("".join(left + right[::-1]))