import sys
import copy
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# CCTV 위치 저장 (1~5인 곳만)
CCTVS = [(i, j) for i in range(n) for j in range(m) if 1 <= graph[i][j] <= 5]

# 방향: 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# CCTV 종류별 방향 조합
cctv_dir = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

# 감시 함수: 방향 리스트에 따라 감시 마킹
def watch(board, x, y, directions):
    for d in directions:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if not (0 <= nx < n and 0 <= ny < m):
                break
            if board[nx][ny] == 6:  # 벽
                break
            if board[nx][ny] == 0:
                board[nx][ny] = '#'

# DFS 탐색
answer = int(1e9)

def dfs(depth, board):
    global answer
    if depth == len(CCTVS):
        # 사각지대 개수 계산
        cnt = sum(row.count(0) for row in board)
        answer = min(answer, cnt)
        return

    x, y = CCTVS[depth]
    cctv_type = graph[x][y]

    for dirs in cctv_dir[cctv_type]:
        temp = copy.deepcopy(board)
        watch(temp, x, y, dirs)
        dfs(depth + 1, temp)

dfs(0, graph)
print(answer)