import sys

input = sys.stdin.readline

# --- 1. 입력 및 초기 설정 ---
n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 초기 방향 (상어 번호 1~m 순서)
initial_dirs = list(map(int, input().split()))

# 우선순위 (상어번호 -> 현재방향 -> 우선순위 리스트)
priorities = {}
for i in range(1, m + 1):
    priorities[i] = []
    for _ in range(4):
        p = list(map(int, input().split()))
        priorities[i].append([x - 1 for x in p])  # 방향 0~3으로 변환

# 냄새 보드 (board[x][y] = [상어번호, 남은시간])
smell_board = [[[0, 0] for _ in range(n)] for _ in range(n)]

# 상어 정보 (sharks[번호] = [x, y, 방향])
sharks = {}
for r in range(n):
    for c in range(n):
        if graph[r][c] > 0:
            shark_num = graph[r][c]
            sharks[shark_num] = [r, c, initial_dirs[shark_num - 1] - 1]

# 방향 벡터 (0:위, 1:아래, 2:왼쪽, 3:오른쪽)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def decrease_smell():
    """모든 냄새를 1씩 감소시키고, 0이 되면 빈칸으로 만듦"""
    for r in range(n):
        for c in range(n):
            if smell_board[r][c][1] > 0:
                smell_board[r][c][1] -= 1
                if smell_board[r][c][1] == 0:
                    smell_board[r][c][0] = 0


def move_sharks():
    """상어를 이동시키고, 충돌 처리 후, 새 냄새를 뿌림"""

    # 1. 모든 상어의 다음 위치 결정
    next_moves = {}
    for shark_num in sorted(sharks.keys()):
        x, y, d = sharks[shark_num]

        # Case 1: 냄새 없는 칸 찾기
        found_empty = False
        for nd in priorities[shark_num][d]:
            nx, ny = x + dx[nd], y + dy[nd]
            if 0 <= nx < n and 0 <= ny < n and smell_board[nx][ny][0] == 0:
                next_moves[shark_num] = [nx, ny, nd]
                found_empty = True
                break

        if found_empty:
            continue

        # Case 2: 자신의 냄새가 있는 칸 찾기
        for nd in priorities[shark_num][d]:
            nx, ny = x + dx[nd], y + dy[nd]
            if 0 <= nx < n and 0 <= ny < n and smell_board[nx][ny][0] == shark_num:
                next_moves[shark_num] = [nx, ny, nd]
                break

    # 2. 냄새 감소 (먼저 감소시켜야 이동 후 새 냄새가 덮어씀)
    decrease_smell()

    # 3. 상어 이동 및 충돌 처리
    new_positions = {}  # 각 칸에 어떤 상어들이 도착했는지 기록
    sharks_to_remove = set()

    for shark_num, move in next_moves.items():
        nx, ny, nd = move
        sharks[shark_num] = [nx, ny, nd]  # 일단 상어 정보 업데이트

        if (nx, ny) in new_positions:  # 해당 칸에 다른 상어가 이미 도착했다면
            sharks_to_remove.add(shark_num)  # 현재 상어는 쫓겨남
        else:
            new_positions[(nx, ny)] = shark_num

    # 쫓겨난 상어 제거
    for shark_num in sharks_to_remove:
        del sharks[shark_num]

    # 4. 살아남은 상어들이 새 냄새 뿌리기
    for shark_num, pos in sharks.items():
        x, y, _ = pos
        smell_board[x][y] = [shark_num, k]


# --- 2. 시뮬레이션 시작 ---
time = 0
# 맨 처음 위치에 냄새 뿌리기
for shark_num, pos in sharks.items():
    x, y, _ = pos
    smell_board[x][y] = [shark_num, k]

while time < 1000:
    # 종료 조건
    if len(sharks) == 1 and 1 in sharks:
        break

    move_sharks()
    time += 1

if len(sharks) == 1 and 1 in sharks:
    print(time)
else:
    print(-1)
    