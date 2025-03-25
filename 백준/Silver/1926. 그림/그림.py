from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    size = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and picture[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                size += 1

    return size


count = 0
max_size = 0

for i in range(n):
    for j in range(m):
        if picture[i][j] == 1 and not visited[i][j]:
            max_size = max(max_size, bfs(i, j))
            count += 1

print(count)
print(max_size)
