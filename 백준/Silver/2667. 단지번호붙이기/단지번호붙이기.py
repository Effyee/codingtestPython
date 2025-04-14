import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
graph=[]
visited=[[False]*n for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int,input().strip())))

def bfs(x,y):
    cnt = 1
    q=deque([[x,y]])
    visited[x][y]=True
    while q:
        x,y=q.popleft()
        dx=[0,0,-1,1]
        dy=[-1,1,0,0]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]==1 and not visited[nx][ny]:
                    visited[nx][ny]=True
                    q.append([nx,ny])
                    cnt += 1
    return cnt

num,cnts=0,[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and not visited[i][j]:
            num+=1
            cnts.append(bfs(i,j))

print(num)
cnts.sort()
for cnt in cnts:
    print(cnt)
