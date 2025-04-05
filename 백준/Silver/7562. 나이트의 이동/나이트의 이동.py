import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append([x, y, 0])
    while q:
        x, y, cnt = q.popleft()
        if tx == x and ty == y:
            print(cnt)
            break
        dx = [-2, -1, +1, +2, +2, +1, -1, -2]
        dy = [+1, +2, +2, +1, -1, -2, -2, -1]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and not graph[nx][ny]:
                graph[nx][ny] = 1
                q.append([nx, ny, cnt + 1])

T = int(input())
for _ in range(T):
    I = int(input())
    graph = [[0] * I for _ in range(I)]
    x, y = map(int, input().split())
    tx, ty = map(int, input().split())
    bfs(x, y)
