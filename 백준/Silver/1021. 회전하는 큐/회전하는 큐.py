# 회전하는 큐
from collections import deque

n, m = map(int, input().split())

num_lst = [i for i in range(1, n+1)]
deque1 = deque(num_lst)
target_lst = map(int, input().split())

count = 0
for target in target_lst:
    pos = deque1.index(target)
    if pos > len(deque1) // 2:
        count += len(deque1) - pos
        deque1.rotate(len(deque1) - pos)
        deque1.popleft()
    else:
        count += pos
        deque1.rotate(-pos)
        deque1.popleft()

print(count)