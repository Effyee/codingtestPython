import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[list(map(int,input().rstrip())) for _ in range(N)]
visited=[[False]*M for _ in range(N)]

answer=int(1e9)
def bfs(x,y):
    global answer
    q=deque([[x,y,1]])
    visited[x][y]=True
    while q:
        x,y,dist=q.popleft()
        if x==N-1 and y==M-1:
            answer=min(answer,dist)
        dx=[0,0,-1,1]
        dy=[-1,1,0,0]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny] and graph[nx][ny]==1:
                    visited[nx][ny]=True
                    q.append([nx,ny,dist+1])

bfs(0,0)

print(answer)