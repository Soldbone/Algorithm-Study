# 큐
import sys
n = int(sys.stdin.readline())

## .split()과 .split(' ')은 다르다. 전자는 '\n'가 포함되지 않고 후자는 포함된다.
my_queue = []
for _ in range(n):
    cmd_lst = sys.stdin.readline().split()
    match cmd_lst[0]:
        case "push":
            my_queue.insert(0, cmd_lst[1])
        case "pop":
            if len(my_queue) > 0:
                print(my_queue.pop())
            else:
                print(-1)
        case "size":
            print(len(my_queue))
        case "empty":
            if len(my_queue):
                print(0)
            else:
                print(1)
        case "front":
            if len(my_queue) > 0:
                print(my_queue[-1])
            else:
                print(-1)
        case "back":
            if len(my_queue) > 0:
                print(my_queue[0])
            else:
                print(-1)
        case _:
            print("!! Something is going wrong !!")
        