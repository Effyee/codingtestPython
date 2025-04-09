import sys
from collections import deque
input=sys.stdin.readline

m,n,k=map(int,input().split())
graph=[[0]*m for _ in range(n)]
l=[]
for _ in range(k):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            graph[i][j]=1

def bfs(i,j):
    q=deque([[i,j]])
    graph[i][j]=1
    cnt=1
    while q:
        x,y=q.popleft()
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==0:
                    graph[nx][ny]=1
                    q.append([nx,ny])
                    cnt+=1
    return cnt


answer=0
l=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            answer+=1
            l.append(bfs(i,j))

print(answer)
l.sort()
print(' '.join(map(str,l)))