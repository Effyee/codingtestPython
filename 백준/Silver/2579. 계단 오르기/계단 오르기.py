import sys
input = sys.stdin.readline

n = int(input())
values = [0]
for _ in range(n):
    values.append(int(input()))

dp = [0] * (n + 1)

if n >= 1:
    dp[1] = values[1]
if n >= 2:
    dp[2] = values[1] + values[2]
if n >= 3:
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2] + values[i], dp[i - 3] + values[i - 1] + values[i])

print(dp[n])
