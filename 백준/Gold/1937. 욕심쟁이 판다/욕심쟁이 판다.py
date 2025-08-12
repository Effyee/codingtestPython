import sys

sys.setrecursionlimit(10 ** 6)  # 재귀 깊이 제한 해제
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > graph[x][y]:
            # (현재까지의 최대 이동 거리)와 (현재 칸 + 다음 칸에서 출발하는 최대 이동 거리) 중 더 큰 값을 선택
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]


answer = 0
# 모든 지점에서 출발하는 경우를 계산
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)