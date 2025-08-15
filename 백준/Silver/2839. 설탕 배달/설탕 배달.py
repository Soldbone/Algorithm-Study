# 설탕 배달

# [16] → 5*2 + 3*2
# [11] → 3: 5*1 + 3*2

N = int(input())

result = -1
num_of_5kg = N//5
for i in range(num_of_5kg, -1, -1):
    remain = (N - 5 * i)
    if ( remain % 3 == 0 ):
        result = i + remain // 3
        break
print(result)
