import sys
input = sys.stdin.readline

n = int(input())
dragons = [list(map(int, input().split())) for _ in range(n)]

# 오, 위, 왼, 아래
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

visited = [[False] * 101 for _ in range(101)]

for dragon in dragons:
    x, y, d, gen = dragon

    # 방향 생성
    curve = [d]
    for _ in range(gen):
        for i in range(len(curve) - 1, -1, -1):
            curve.append((curve[i] + 1) % 4)

    # 좌표 따라가며 visited 표시
    visited[x][y] = True
    for dir in curve:
        x += dx[dir]
        y += dy[dir]
        visited[x][y] = True

# 정사각형 개수 세기
count = 0
for i in range(100):
    for j in range(100):
        if visited[i][j] and visited[i+1][j] and visited[i][j+1] and visited[i+1][j+1]:
            count += 1

print(count)