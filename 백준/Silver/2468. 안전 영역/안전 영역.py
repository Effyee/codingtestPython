import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

max_height = max(map(max, arr))
answer = 0

def bfs(x, y, visited, height):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and arr[nx][ny] > height:
                    visited[nx][ny] = True
                    q.append((nx, ny))

for h in range(0, max_height):
    visited = [[False]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] > h:
                bfs(i, j, visited, h)
                count += 1
    answer = max(answer, count)

print(answer)