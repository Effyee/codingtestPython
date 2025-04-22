from collections import deque
from itertools import combinations

# 입력
n, m, g, r = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(n)]

# 배양액을 뿌릴 수 있는 위치
poses = [(x, y) for x in range(n) for y in range(m) if garden[x][y] == 2]

pos_combinations = []

# G + R 개 조합 만들기
def backtrack(idx, li):
    if len(li) == g + r:
        pos_combinations.append(li[:])
        return
    if idx == len(poses):
        return
    backtrack(idx + 1, li + [poses[idx]])
    backtrack(idx + 1, li)

backtrack(0, [])

# BFS 시뮬레이션 함수
def simulate(green, red):
    q = deque()
    color = [[-1] * m for _ in range(n)]  # -1: 없음, 1: 초록, 2: 빨강, 3: 꽃
    time = [[-1] * m for _ in range(n)]

    for gx, gy in green:
        q.append((gx, gy))
        color[gx][gy] = 1
        time[gx][gy] = 0

    for rx, ry in red:
        q.append((rx, ry))
        color[rx][ry] = 2
        time[rx][ry] = 0

    flowers = 0
    while q:
        x, y = q.popleft()
        if color[x][y] == 3:
            continue
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and garden[nx][ny] != 0:
                if color[nx][ny] == -1:
                    color[nx][ny] = color[x][y]
                    time[nx][ny] = time[x][y] + 1
                    q.append((nx, ny))
                elif (color[nx][ny] != color[x][y] and time[nx][ny] == time[x][y] + 1 and color[nx][ny] != 3):
                    color[nx][ny] = 3
                    flowers += 1
    return flowers

# 최대 꽃 개수 계산
answer = 0
for comb in pos_combinations:
    for green in combinations(comb, g):
        red = [p for p in comb if p not in green]
        flowers = simulate(green, red)
        answer = max(answer, flowers)

print(answer)
