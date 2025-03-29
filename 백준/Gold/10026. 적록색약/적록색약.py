import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(str,input().strip())))

visited=[[False]*len(graph[0]) for _ in range(N)]

def bfs(x,y):
    q=deque([(x,y,graph[x][y])])
    while q:
        x,y,color=q.popleft()
        dx=[0,0,-1,1]
        dy=[-1,1,0,0]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<len(graph[0]):
                if not visited[nx][ny] and graph[nx][ny]==color:
                    visited[nx][ny]=True
                    q.append((nx,ny,color))
    return

def grbfs(x,y):
    q=deque([(x,y,graph[x][y])])
    while q:
        x,y,color=q.popleft()
        dx=[0,0,-1,1]
        dy=[-1,1,0,0]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<len(graph[0]):
                if color=='R' or color=='G':
                    if not visited[nx][ny] and graph[nx][ny] in ['R','G']:
                        visited[nx][ny] = True
                        q.append((nx, ny, color))
                else:
                    if not visited[nx][ny] and graph[nx][ny]==color:
                        visited[nx][ny]=True
                        q.append((nx,ny,color))
    return

ans1,ans2=0,0

for x in range(N):
    for y in range(len(graph[0])):
        if not visited[x][y]:
            bfs(x,y)
            ans1+=1

visited=[[False]*len(graph[0]) for _ in range(N)]

for x in range(N):
    for y in range(len(graph[0])):
        if not visited[x][y]:
            grbfs(x,y)
            ans2+=1

print(ans1,ans2)