import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
maps = [[0] * (n + 1) for _ in range(n + 1)]

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())  # 변수 이름을 n, m에서 a, b로 변경해줍니다.
    maps[a][b] = 2

l = int(input())
info = {}

for _ in range(l):
    time, direction = input().split()
    info[int(time)] = direction

# 초기화
d = 0  # 방향
dx = [0, 1, 0, -1]  # 우, 하, 좌, 상
dy = [1, 0, -1, 0]
x, y = 1, 1  # 시작 위치
snakes = deque([(x, y)])
time = 0  # 시간 초기화

while True:
    nx = x + dx[d]
    ny = y + dy[d]
    time += 1  # 시간 증가

    if 1 <= nx <= n and 1 <= ny <= n and (nx, ny) not in snakes:
        # 사과가 없다면
        if maps[nx][ny] != 2:
            snakes.popleft()
        else:
            maps[nx][ny] = 0  # 사과를 먹으면 맵에서 사과를 제거합니다.
        x, y = nx, ny
        snakes.append((nx, ny))
    else:
        break  # 벽 또는 자기 자신의 몸과 부딪히면 게임 종료

    if time in info.keys():
        if info[time] == 'D':
            d = (d + 1) % 4
        elif info[time] == 'L':
            d = (d - 1) % 4

print(time)
