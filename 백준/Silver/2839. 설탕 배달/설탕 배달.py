N = int(input())

result = -1
num_of_5kg = N//5
for i in range(num_of_5kg, -1, -1):
    remain = (N - 5 * i)
    num_of_3kg = remain // 3
    if ( remain - 3 * num_of_3kg == 0 ):
        result = i + num_of_3kg
        break
print(result)