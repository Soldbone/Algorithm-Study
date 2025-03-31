# 나무 조각
woods = list(map(int, input().split()))

while woods != [1, 2, 3, 4, 5]:
    for i in range(1, len(woods)):
        if woods[i-1] > woods[i]:
            woods[i-1], woods[i] = woods[i], woods[i-1]
            print(*woods, sep=' ')