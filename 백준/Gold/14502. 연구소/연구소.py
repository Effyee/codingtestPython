import sys
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(graph):
    q = deque([(x, y) for x in range(n) for y in range(m) if graph[x][y] == 2])

    while q:
        x, y = q.popleft()
        for (nx, ny) in zip ([x+1, x, x-1, x], [y, y+1, y, y-1]):
            if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny]:  # 수정된 범위 확인 부분
                graph[nx][ny] = 2
                q.append((nx, ny))

    count = sum([i.count(0) for i in graph])
    return count  # 결과값을 반환하도록 수정

x_y = [(x, y) for x in range(n) for y in range(m) if not graph[x][y]]
answer = 0

for c in combinations(x_y, 3):
    tmp = copy.deepcopy(graph)  # 깊은 복사를 사용하여 임시 그래프 생성
    for x, y in c:
        tmp[x][y] = 1  # 임시 그래프에 벽 설치
    answer = max(answer, bfs(tmp))  # 임시 그래프를 bfs 함수에 전달

print(answer)
