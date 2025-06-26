import sys
input = sys.stdin.readline

n = int(input())
t = [0]
p = [0]

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

dp = [0] * (n + 2)

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])
    last_day = i + t[i]
    if last_day <= n + 1:
        dp[last_day] = max(dp[last_day], dp[i] + p[i])

print(max(dp))
