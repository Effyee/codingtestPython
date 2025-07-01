import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

# visited[x][y][0] -> 벽 안 부심 / visited[x][y][1] -> 벽 한 번 부심
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

def bfs(x, y, z):
    q = deque()
    q.append((x, y, z))
    visited[x][y][z] = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while q:
        x, y, z = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 벽이고 아직 벽 부순 적 없음
                if graph[nx][ny] == 1 and z == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][z] + 1
                    q.append((nx, ny, 1))
                # 벽이 아니고 방문한 적 없음
                elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx, ny, z))

    return -1

print(bfs(0, 0, 0))
