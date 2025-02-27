import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# dp 배열을 0으로 초기화
dp = [[[0] * N for _ in range(N)] for _ in range(3)]

def solution():
    # 첫 시작점 초기화 (가로 방향)
    dp[0][0][1] = 1
    
    # 첫 번째 행 (가로 방향으로만 이동 가능)
    for i in range(2, N):
        if graph[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]

    for r in range(1, N):
        for c in range(1, N):
            if graph[r][c] == 1:
                continue  # 벽이면 건너뛴다
            
            # 가로 (→) 방향 이동 가능 여부
            if graph[r][c - 1] == 0:
                dp[0][r][c] = dp[0][r][c - 1] + dp[2][r][c - 1]

            # 세로 (↓) 방향 이동 가능 여부
            if graph[r - 1][c] == 0:
                dp[1][r][c] = dp[1][r - 1][c] + dp[2][r - 1][c]

            # 대각선 (↘) 방향 이동 가능 여부
            if graph[r - 1][c] == 0 and graph[r][c - 1] == 0 and graph[r - 1][c - 1] == 0:
                dp[2][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

solution()
print(sum(dp[i][N - 1][N - 1] for i in range(3)))
