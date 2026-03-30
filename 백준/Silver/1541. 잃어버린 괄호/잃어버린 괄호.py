expression = input()
split_minus = expression.split("-")

total_sum = sum(map(int, split_minus[0].split("+")))

for part in split_minus[1:]:
    total_sum -= sum(map(int, part.split("+")))

print(total_sum)