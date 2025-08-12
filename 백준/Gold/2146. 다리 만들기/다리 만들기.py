import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 1. 섬의 번호 매기기 (Labeling)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs_labeling(x, y, island_num):
    q = deque([(x, y)])
    graph[x][y] = island_num
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = island_num
                q.append((nx, ny))


# 섬 번호는 2부터 시작
cnt = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs_labeling(i, j, cnt)
            cnt += 1


# 2. 가장 짧은 다리 찾기
def find_shortest_bridge(start_island_num):
    dist = [[-1] * n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if graph[i][j] == start_island_num:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 다른 섬에 도착했다면, 현재 다리 길이를 반환
                if graph[nx][ny] > 0 and graph[nx][ny] != start_island_num:
                    return dist[x][y]
                # 바다이고 아직 방문 안 했다면, 다리를 놓음
                if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    # 다른 섬을 찾지 못했다면 무한대 반환
    return float('inf')


# 3. 메인 로직
answer = float('inf')
# 모든 섬에 대해(2번 ~ cnt-1번) 최단 다리 길이를 탐색
for island_num in range(2, cnt):
    answer = min(answer, find_shortest_bridge(island_num))

print(answer)
