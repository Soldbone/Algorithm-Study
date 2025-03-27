# 괄호
import sys

T = int(input())

for _ in range(T):
    input_ps = sys.stdin.readline().strip()

    stk1 = []
    IS_ALREADY_NO = False
    for p in input_ps:
        if p == '(':
            stk1.append(p)
        elif len(stk1) > 0:
            stk1.pop()
        else:
            print("NO")
            IS_ALREADY_NO = True
            break
    
    if stk1:
        print("NO")
    elif not IS_ALREADY_NO:
        print("YES")
    # else (IS_ALREADY_NO): pass (already processed)