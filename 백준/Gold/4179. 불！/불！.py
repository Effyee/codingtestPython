import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    q = deque()

    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'F':
                q.append((i, j, 'F', 0))

    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'J':
                if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                    return 1
                q.append((i, j, 'J', 1))

    while q:
        x, y, kind, time = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if kind == 'F':
                    if graph[nx][ny] == '.' or graph[nx][ny] == 'J':
                        graph[nx][ny] = 'F'
                        q.append((nx, ny, 'F', time + 1))
                else:
                    if graph[nx][ny] == '.':
                        if nx == 0 or nx == r - 1 or ny == 0 or ny == c - 1:
                            return time + 1
                        graph[nx][ny] = 'J'
                        q.append((nx, ny, 'J', time + 1))

    return "IMPOSSIBLE"

print(bfs())
