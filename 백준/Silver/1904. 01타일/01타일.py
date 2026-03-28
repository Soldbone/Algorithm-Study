N = int(input())

a = b = 1
for _ in range(2, N + 1):
    a, b = b % 15746, (a + b) % 15746
print(b)