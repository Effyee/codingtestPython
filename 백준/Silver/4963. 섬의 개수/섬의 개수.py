import sys
from collections import deque
input=sys.stdin.readline

def bfs(x,y,graph,visited):
    global answer
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    q=deque([[x,y]])
    visited[x][y]=True
    while q:
        x,y=q.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w:
                if not visited[nx][ny] and graph[nx][ny]==1:
                    visited[nx][ny]=True
                    q.append([nx,ny])
    return

while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    answer = 0
    graph=[list(map(int,input().split())) for _ in range(h)]
    visited=[[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1 and not visited[i][j]:
                bfs(i,j,graph,visited)
                answer+=1
    print(answer)