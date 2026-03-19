import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[list(map(int,input().strip())) for _ in range(n)]
visited=[[[False,False] for _ in range(m)] for _ in range(n)]

def bfs():
    q=deque()
    visited[0][0][0]=True
    q.append((0,0,1,0))
    while q:
        x,y,dist,flag=q.popleft()
        if x==n-1 and y==m-1:
            return dist
        dx=[0,0,-1,1]
        dy=[-1,1,0,0]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not flag:
                    if not visited[nx][ny][0]:
                        if graph[nx][ny]==0:
                            visited[nx][ny][0]=True
                            q.append((nx,ny,dist+1,0))
                        else:
                            visited[nx][ny][1]=True
                            q.append((nx,ny,dist+1,1))
                else:
                    if not visited[nx][ny][1] and graph[nx][ny] == 0:
                        visited[nx][ny][1] = True
                        q.append((nx, ny, dist + 1, 1))

    return int(1e9)

answer=bfs()
if answer==int(1e9):
    print(-1)
else:
    print(answer)