import sys
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def count_v(graph):
    return sum(row.count(0) for row in graph)


pos = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]
walls = list(combinations(pos, 3))

answer = 0  # 최대값을 찾아야 하므로 0으로 초기화


def bfs():
    global answer
    for wall in walls:
        cgraph = copy.deepcopy(graph)
        for x, y in wall:
            cgraph[x][y] = 1

        q = deque([(i, j) for i in range(n) for j in range(m) if cgraph[i][j] == 2])
        while q:
            x, y = q.popleft()
            for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and cgraph[nx][ny] == 0:
                    cgraph[nx][ny] = 2
                    q.append((nx, ny))

        new_answer = count_v(cgraph)
        answer = max(answer, new_answer)


bfs()
print(answer)