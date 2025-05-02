import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

# 주사위 상태: [윗, 북, 동, 서, 남, 바닥]
dice = [0] * 6

# 동, 서, 북, 남 → 인덱스 0,1,2,3
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for cmd in commands:
    dir = cmd - 1
    nx = x + dx[dir]
    ny = y + dy[dir]

    if not (0 <= nx < n and 0 <= ny < m):
        continue  # 바깥으로 나가면 무시

    # 주사위 회전
    if dir == 0:  # 동
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif dir == 1:  # 서
        dice[0], dice[3], dice[5], dice[2] = dice[2], dice[0], dice[3], dice[5]
    elif dir == 2:  # 북
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]
    elif dir == 3:  # 남
        dice[0], dice[4], dice[5], dice[1] = dice[1], dice[0], dice[4], dice[5]

    # 복사 조건
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[5]
    else:
        dice[5] = graph[nx][ny]
        graph[nx][ny] = 0

    # 위치 업데이트
    x, y = nx, ny

    print(dice[0])  # 윗면 출력
