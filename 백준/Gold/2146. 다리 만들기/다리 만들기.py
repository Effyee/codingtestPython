import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]

# 1. 섬 넘버링
def bfs(x,y,cnt):
    q=deque()
    q.append([x,y,cnt])
    graph[x][y]=cnt
    while q:
        x,y,cnt=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]==1:
                    graph[nx][ny]=cnt
                    q.append((nx,ny,cnt))
    return

cnt=2
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            bfs(i,j,cnt)
            cnt+=1

visited=[[False]*n for _ in range(n)]
def bfs2(x,y,island):
    q=deque()
    visited[x][y]=True
    q.append([x,y,0,island])
    while q:
        x,y,dist,island=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and graph[nx][ny]==0:
                    visited[nx][ny]=True
                    q.append([nx,ny,dist+1,island])
                elif graph[nx][ny]!=island and graph[nx][ny]!=0:
                    return dist
    return -1

ans = 1e9
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            visited = [[False]*n for _ in range(n)]
            re = bfs2(i, j, graph[i][j])
            if re != -1:
                ans = min(ans, re)

print(ans)
