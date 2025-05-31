# 시험 감독
# 총감독관은 반드시 1명 존재해야 하는 듯하다.
import sys
input = sys.stdin.readline

N = int(input())
A_lst = list(map(int, input().split()))
B, C = map(int, input().split())

def calc_num_of_necessary_supervisor():
    num_of_necessary_supervisor = 0
    for A in A_lst:
        # 총감독관만으로 한 시험장의 인원을 모두 감시 가능한 경우
        if A - B <= 0:
            num_of_necessary_supervisor += 1
        # 총감독관으로 부족한 경우 (모두 감시 가능할 때까지 부감독관 배치)
        else:
            A_after_head = A - B
            num_of_necessary_supervisor += ((A_after_head // C + 1) + 1) if (A_after_head % C != 0) else (A_after_head // C + 1)
    return num_of_necessary_supervisor


print(calc_num_of_necessary_supervisor())
