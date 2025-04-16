n = int(input())
dp = [False] * (1001)

dp[1] = True      # SK
dp[2] = False     # CY
dp[3] = True      # SK
dp[4] = True      # SK

for i in range(5, n + 1):
    dp[i] = not dp[i - 1] or not dp[i - 3] or not dp[i - 4]

print("SK" if dp[n] else "CY")
