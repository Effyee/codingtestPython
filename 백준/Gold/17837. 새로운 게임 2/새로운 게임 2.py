import sys
input = sys.stdin.readline

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# 0: 흰색, 1: 빨강, 2: 파랑

# 방향 (1: 오른, 2: 왼, 3: 위, 4: 아래)
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

# 말 정보: 번호 -> [x, y, direction]
pawns = {}
# 체스판 스택: (x,y) -> 말 번호 리스트
stacks = [[[] for _ in range(n)] for _ in range(n)]

for num in range(1, k+1):
    x, y, d = map(int, input().split())
    x -= 1; y -= 1  # 0-indexed
    pawns[num] = [x, y, d]
    stacks[x][y].append(num)

# 방향 반대
reverse = {1:2, 2:1, 3:4, 4:3}

time = 0
while time <= 1000:
    time += 1
    for num in range(1, k+1):
        x, y, d = pawns[num]
        # 현재 말의 위치에서 스택 찾기
        idx = stacks[x][y].index(num)
        moving = stacks[x][y][idx:]  # 이동할 말들
        stacks[x][y] = stacks[x][y][:idx]  # 남은 말

        nx = x + dx[d]
        ny = y + dy[d]

        # 파랑 혹은 보드 밖
        if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
            d = reverse[d]
            pawns[num][2] = d  # 방향 갱신
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
                # 이동 불가
                stacks[x][y] += moving
                continue

        # 흰색
        if board[nx][ny] == 0:
            stacks[nx][ny] += moving
        # 빨강
        elif board[nx][ny] == 1:
            stacks[nx][ny] += moving[::-1]

        # 말 위치 갱신
        for m in moving:
            pawns[m][0] = nx
            pawns[m][1] = ny

        # 종료 조건
        if len(stacks[nx][ny]) >= 4:
            print(time)
            exit(0)

print(-1)
