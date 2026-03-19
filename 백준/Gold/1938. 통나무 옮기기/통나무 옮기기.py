import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

B, E = [], []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'B':
            B.append((i, j))
        elif graph[i][j] == 'E':
            E.append((i, j))

def find_dir(A):
    if A[0][0] == A[1][0] == A[2][0]:
        return A[1][0], A[1][1], 0
    return A[1][0], A[1][1], 1

sx, sy, sd = find_dir(B)
ex, ey, ed = find_dir(E)

def can_move(x, y):
    return 0 <= x < n and 0 <= y < n and graph[x][y] != '1'

def can_rotate(x, y):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if not (0 <= i < n and 0 <= j < n and graph[i][j] != '1'):
                return False
    return True

visited = [[[False, False] for _ in range(n)] for _ in range(n)]

def bfs():
    q = deque()
    visited[sx][sy][sd] = True
    q.append((sx, sy, sd, 0))
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    while q:
        x, y, d, count = q.popleft()
        if x == ex and y == ey and d == ed:
            return count
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if d == 0: # 가로일 때
                # 가로로 놓인 세 칸(ny-1, ny, ny+1)이 모두 이동 가능한지 확인
                if can_move(nx, ny-1) and can_move(nx, ny) and can_move(nx, ny+1):
                    if not visited[nx][ny][d]:
                        visited[nx][ny][d] = True
                        q.append((nx, ny, d, count + 1))
            else: # 세로일 때
                # 세로로 놓인 세 칸(nx-1, nx, nx+1)이 모두 이동 가능한지 확인
                if can_move(nx-1, ny) and can_move(nx, ny) and can_move(nx+1, ny):
                    if not visited[nx][ny][d]:
                        visited[nx][ny][d] = True
                        q.append((nx, ny, d, count + 1))

        # 2. 회전 (이동 루프 밖에서 현재 좌표 x, y 기준으로 실행)
        if can_rotate(x, y):
            nd = 1 - d
            if not visited[x][y][nd]:
                visited[x][y][nd] = True
                q.append((x, y, nd, count + 1))

    return 0

print(bfs())