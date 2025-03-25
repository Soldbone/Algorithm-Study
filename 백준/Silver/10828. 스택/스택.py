import sys
N = int(sys.stdin.readline())
stk1 = []
for i in range(N):
    cmd_lst = sys.stdin.readline().split()
    if len(cmd_lst) > 1:
        stk1.append(int(cmd_lst[1]))
    elif cmd_lst[0] == "pop":
        if len(stk1) > 0:
            print(stk1.pop())
        else:
            print(-1)
    elif cmd_lst[0] == "size":
        print(len(stk1))
    elif cmd_lst[0] == "empty":
        if len(stk1):
            print(0)
        else:
            print(1)
    elif cmd_lst[0] == "top":
        if len(stk1) > 0:
            print(stk1[-1])
        else:
            print(-1)