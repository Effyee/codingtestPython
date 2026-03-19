import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

# B, E 좌표 찾기
B = []
E = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'B':
            B.append((i,j))
        elif graph[i][j] == 'E':
            E.append((i,j))

# 중심과 방향 구하기
def get_state(arr):
    arr.sort()
    if arr[0][0] == arr[1][0] == arr[2][0]:  # 가로
        return arr[1][0], arr[1][1], 0
    else:  # 세로
        return arr[1][0], arr[1][1], 1

sx, sy, sdir = get_state(B)
ex, ey, edir = get_state(E)

visited = [[[0]*2 for _ in range(n)] for _ in range(n)]

def can_move(x, y):
    return 0 <= x < n and 0 <= y < n and graph[x][y] != '1'

def can_rotate(x, y):
    # 중심 기준 3x3 확인
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if not (0 <= i < n and 0 <= j < n):
                return False
            if graph[i][j] == '1':
                return False
    return True

def bfs():
    q = deque()
    q.append((sx, sy, sdir, 0))
    visited[sx][sy][sdir] = 1

    while q:
        x, y, d, dist = q.popleft()

        if (x, y, d) == (ex, ey, edir):
            return dist

        # 상하좌우 이동
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy

            if d == 0:  # 가로
                if (can_move(nx, ny-1) and 
                    can_move(nx, ny) and 
                    can_move(nx, ny+1)):
                    if not visited[nx][ny][d]:
                        visited[nx][ny][d] = 1
                        q.append((nx, ny, d, dist+1))
            else:  # 세로
                if (can_move(nx-1, ny) and 
                    can_move(nx, ny) and 
                    can_move(nx+1, ny)):
                    if not visited[nx][ny][d]:
                        visited[nx][ny][d] = 1
                        q.append((nx, ny, d, dist+1))

        # 회전
        if can_rotate(x, y):
            nd = 1 - d
            if not visited[x][y][nd]:
                visited[x][y][nd] = 1
                q.append((x, y, nd, dist+1))

    return 0

print(bfs())