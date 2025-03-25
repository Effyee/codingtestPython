import sys
from collections import deque
input=sys.stdin.readline
m,n=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

riped=deque([(x,y,0) for x in range(n) for y in range(m) if graph[x][y]==1])

answer=-1
def bfs():
    global answer
    while riped:
        x,y,days=riped.popleft()
        answer=max(answer,days)
        dx=[0,0,-1,1]
        dy=[-1,1,0,0]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==0:
                    graph[nx][ny]=1
                    riped.append((nx,ny,days+1))

bfs()

for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            print(-1)
            exit()
print(answer)