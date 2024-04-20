import sys
from collections import deque

input = sys.stdin.readline

# 그래프 초기화
n = int(input())
graph = [[0] * n for _ in range(n)]

# 사과 배치
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 2

# 이동
info = {}
move = int(input())

for _ in range(move):
    second, direction = input().split()
    info[int(second)] = direction

# 초기화
direction = 0
snakes = deque([(0, 0)])
x, y = 0, 0
graph[x][y] = 1  # 뱀의 초기 위치 표시
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
time = 0

while True:
    # 해당 시간에 방향을 바꿔야한다면
    if time in info.keys():
        if info[time] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

    nx = x + dx[direction]
    ny = y + dy[direction]
    time += 1
    # 그래프의 범위를 벗어나거나 해당 공간에 몸통이 있으면
    if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 1:
        print(time)
        break
    # 이동하는 공간이 사과가 있다면
    if graph[nx][ny] == 2:
        graph[nx][ny] = 1
        snakes.append((nx, ny))
    # 사과가 없다면
    else:
        graph[nx][ny] = 1
        snakes.append((nx, ny))
        tail_x, tail_y = snakes.popleft()
        graph[tail_x][tail_y] = 0
    x, y = nx, ny
