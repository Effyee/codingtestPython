import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    time, price = map(int, input().split())
    l.append((time, price))

dp = [0] * (n + 2)

for i in range(1, n + 1):
    time, price = l[i - 1]
    # 상담을 할 수 있는 경우
    if i + time - 1 <= n:
        dp[i + time] = max(dp[i + time], dp[i] + price)
    # 상담을 하지 않는 경우
    dp[i + 1] = max(dp[i + 1], dp[i])

# 최대 수익은 dp[n + 1]에 저장
print(max(dp))
