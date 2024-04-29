from itertools import combinations
from collections import deque
import copy

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(input().split()))

def bfs(graph):
    q = deque([(x, y) for x in range(n) for y in range(n) if graph[x][y] == 'T'])
    directions = [(-1,0), (1,0), (0,-1), (0,1)] # 상, 하, 좌, 우

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 'O': # 장애물에 부딪히면 중지
                    break
                if graph[nx][ny] == 'S': # 학생을 발견하면 False 반환
                    return False
                nx += dx
                ny += dy
    return True

x_y = [(x, y) for x in range(n) for y in range(n) if graph[x][y] == 'X']
result = 'NO'

for c in combinations(x_y, 3):
    tmp_graph = copy.deepcopy(graph)
    for x, y in c:
        tmp_graph[x][y] = 'O'
    if bfs(tmp_graph):
        result = 'YES'
        break

print(result)
