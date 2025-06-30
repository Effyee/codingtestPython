import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
graph=[list(map(str,input().rstrip())) for _ in range(n)]
visited=[[False]*(n) for _ in range(n)]

def bfs(x,y):
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    q=deque([[x,y]])
    visited[x][y] = True
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if graph[x][y]=='R':
                    if graph[nx][ny]=='R' or graph[nx][ny]=='G':
                        visited[nx][ny] = True
                        q.append([nx,ny])
                elif graph[x][y]=='G':
                    if graph[nx][ny]=='R' or graph[nx][ny]=='G':
                        visited[nx][ny] = True
                        q.append([nx,ny])
                else:
                    if graph[nx][ny]=='B':
                        visited[nx][ny] = True
                        q.append([nx,ny])
    return 1

answer=0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            answer+=1

visited=[[False]*(n) for _ in range(n)]

def bfs_RGB(x,y):
    q=deque([[x,y]])
    visited[x][y] = True
    while q:
        x,y=q.popleft()
        dx=[0,0,-1,1]
        dy=[-1,1,0,0]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if graph[x][y]==graph[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx,ny])

    return

answer2=0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs_RGB(i,j)
            answer2+=1

print(answer2, answer)