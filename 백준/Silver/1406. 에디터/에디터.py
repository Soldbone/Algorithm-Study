import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []

for _ in range(int(input())):
    cmd = input().rstrip()

    if cmd[0] == 'L':
        if left:
            right.append(left.pop())
    elif cmd[0] == 'D':
        if right:
            left.append(right.pop())
    elif cmd[0] == 'B':
        if left:
            left.pop()
    else:  # P x
        left.append(cmd[2])

left.extend(reversed(right))
print(''.join(left))