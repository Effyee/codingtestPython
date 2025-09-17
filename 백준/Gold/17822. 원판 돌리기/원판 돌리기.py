import sys
from collections import deque
input = sys.stdin.readline

n,m,t = map(int,input().split())
board = [[0]*m] + [list(map(int,input().split())) for _ in range(n)]
move = [list(map(int,input().split())) for _ in range(t)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y,visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    s = {(x,y)}
    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = (cy + dy[i]) % m   # 원판은 원형
            if 1 <= nx <= n and not visited[nx][ny] and board[nx][ny] == board[x][y]:
                visited[nx][ny] = True
                s.add((nx,ny))
                q.append((nx,ny))
    return s

for x,d,k in move:
    # 1. 회전
    for i in range(x, n+1, x):
        k %= m
        if d == 0:  # 시계
            board[i] = board[i][-k:] + board[i][:-k]
        else:       # 반시계
            board[i] = board[i][k:] + board[i][:k]

    # 2. 인접 같은 수 찾기
    # 2. 인접 같은 수 찾기
    visited = [[False] * m for _ in range(n + 1)]
    remove = set()
    for a in range(1, n + 1):
        for b in range(m):
            if board[a][b] != 0 and not visited[a][b]:
                group = bfs(a, b, visited)
                if len(group) > 1:
                    remove |= group

    if remove:
        for x, y in remove:
            board[x][y] = 0
    else:
        total = 0
        cnt = 0
        for i in range(1, n + 1):
            for j in range(m):
                if board[i][j] != 0:
                    total += board[i][j]
                    cnt += 1
        if cnt > 0:
            average = total / cnt
            for i in range(1, n + 1):
                for j in range(m):
                    if board[i][j] == 0: continue
                    if board[i][j] > average:
                        board[i][j] -= 1
                    elif board[i][j] < average:
                        board[i][j] += 1

answer=0
for i in range(1,n+1):
    for j in range(m):
        answer+=board[i][j]
print(answer)
