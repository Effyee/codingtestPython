import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def melt():
    melt_map = [[0]*m for _ in range(n)]

    # 주변 바다 개수 세기
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                count = 0
                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    if 0 <= ni < n and 0 <= nj < m:
                        if graph[ni][nj] == 0:
                            count += 1
                melt_map[i][j] = count

    # 동시에 녹이기
    for i in range(n):
        for j in range(m):
            graph[i][j] = max(0, graph[i][j] - melt_map[i][j])

def bfs(i, j, visited):
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] > 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))

def count_icebergs():
    visited = [[False]*m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                count += 1
    return count

year = 0
while True:
    components = count_icebergs()
    if components == 0:
        print(0)
        break
    if components >= 2:
        print(year)
        break
    melt()
    year += 1
