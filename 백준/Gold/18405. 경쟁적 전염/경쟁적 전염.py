import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

def bfs():
    virus = deque([(i, j, graph[i][j], 0) for i in range(n) for j in range(n) if graph[i][j] > 0])
    virus = deque(sorted(virus, key=lambda x: x[2]))

    while virus:
        x, y, virus_num, time = virus.popleft()
        if time == s:
            break
        for (nx, ny) in zip([x, x, x + 1, x - 1], [y + 1, y - 1, y, y]):
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = virus_num
                virus.append((nx, ny, virus_num, time + 1))

bfs()
print(graph[x - 1][y - 1])
