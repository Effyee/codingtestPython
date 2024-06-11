from collections import deque

def bfs(x,y,maps):
    n=len(maps)
    m=len(maps[0])
    visited=[[False]*m for _ in range(n)]

    q=deque([(x,y,1)])
    visited[x][y]=True

    dx=[0,0,-1,1]
    dy=[-1,1,0,0]

    while q:
        x,y,dist=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx==n-1 and ny==m-1:
                return dist+1
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if maps[nx][ny]==1:
                    visited[nx][ny]=True
                    q.append((nx,ny,dist+1))

def solution(maps):
    result=bfs(0,0,maps)
    if result!=None:
        return result
    return -1