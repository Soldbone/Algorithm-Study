import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

preorder = []
while True:
    try:
        line = input().strip()
        if not line:
            break
        preorder.append(int(line))
    except:
        break

idx = 0
n = len(preorder)
result = []


def build(lower, upper):
    global idx

    if idx >= n:
        return

    value = preorder[idx]

    if not (lower < value < upper):
        return

    idx += 1
    build(lower, value)  # 왼쪽
    build(value, upper)  # 오른쪽
    result.append(value)  # 후위 순회


build(float("-inf"), float("inf"))
print("\n".join(map(str, result)))