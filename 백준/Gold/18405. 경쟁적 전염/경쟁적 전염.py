import sys
from collections import deque

n, k = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

def bfs():
    virus = [(i, j, graph[i][j], 0) for i in range(n) for j in range(n) if graph[i][j] > 0]
    virus = deque(sorted(virus, key=lambda x: x[2])) # 여기서 정렬되어 큐에 추가되어야 합니다.
    while virus:
        x, y, virus_num, second = virus.popleft()
        if second == s:
            break
        for nx, ny in ((x, y-1), (x, y+1), (x+1, y), (x-1, y)):
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = virus_num
                virus.append((nx, ny, virus_num, second + 1))

bfs()
print(graph[x-1][y-1])
