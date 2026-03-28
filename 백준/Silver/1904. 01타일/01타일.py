N = int(input())

a = b = 1
for _ in range(2, N + 1):
    a, b = b, (a + b) % 15746
print(b)