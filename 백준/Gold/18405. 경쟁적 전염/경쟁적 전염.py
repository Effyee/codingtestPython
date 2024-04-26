from collections import deque

n, k = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    q = deque()
    # 초기 바이러스 위치를 큐에 추가
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                q.append((i, j, graph[i][j], 0))  # (x, y, virus, time)
    # 바이러스 번호 순으로 정렬
    q = deque(sorted(q, key=lambda x: x[2]))

    while q:
        x, y, virus, time = q.popleft()
        if time == s:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((nx, ny, virus, time + 1))

bfs()
print(graph[x-1][y-1])
