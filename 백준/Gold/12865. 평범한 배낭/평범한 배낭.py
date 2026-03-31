N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (K + 1)

for i in range(len(items)):
    for w in range(K, 0, -1):
        if w >= items[i][0]:
            dp[w] = max(dp[w], dp[w - 1], dp[w - items[i][0]] + items[i][1])
print(dp[K])
