import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())

dp = [INF] * (n+1)
parent = [-1] * (n+1)

dp[1] = 0  # 1은 연산이 0회

for i in range(2, n+1):
    # 1 빼기
    dp[i] = dp[i-1] + 1
    parent[i] = i-1

    # 2로 나누기
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        parent[i] = i//2

    # 3으로 나누기
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        parent[i] = i//3

# 연산 횟수 출력
print(dp[n])

# 경로 복원
path = []
cur = n
while cur != -1:
    path.append(cur)
    cur = parent[cur]

print(*path)
