from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    union = [(x, y)]
    total_pop = graph[x][y]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    union.append((nx, ny))
                    total_pop += graph[nx][ny]

    # 연합 인구 조정
    for i, j in union:
        graph[i][j] = total_pop // len(union)
    return len(union)


def process():
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j, visited) > 1:  # 연합이 형성되어 인구 이동 발생
                    count += 1
    return count


days = 0
while True:
    if process() == 0:  # 더 이상 인구 이동이 없을 때
        break
    days += 1

print(days)
