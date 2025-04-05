import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

ans = "IMPOSSIBLE"

def bfs():
    q = deque()
    visited = [[False] * m for _ in range(n)]

    # 불 먼저
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'F':
                q.append([-1, i, j])
    # 지훈이 나중
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'J':
                q.append([0, i, j])
                visited[i][j] = True

    global ans
    while q:
        time, x, y = q.popleft()

        if time >= 0 and (x == 0 or x == n - 1 or y == 0 or y == m - 1):
            ans = time + 1
            return

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if time == -1 and graph[nx][ny] in ['.', 'J']:
                    graph[nx][ny] = 'F'
                    q.append([-1, nx, ny])
                elif time >= 0 and graph[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    graph[nx][ny] = 'J'
                    q.append([time + 1, nx, ny])

bfs()
print(ans)
