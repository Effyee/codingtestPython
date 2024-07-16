import sys
import copy
from collections import deque
from itertools import combinations

input=sys.stdin.readline
n,m=map(int,input().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))

def bfs(x,y,g):
    q = deque([(x, y) for x in range(n) for y in range(m) if graph[x][y] == 2])

    while q:
        x,y=q.popleft()
        for dx,dy in zip([0,0,-1,1],[-1,1,0,0]):
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<=ny<m and  g[nx][ny]==0:
                g[nx][ny]=2
                q.append((nx,ny))
    return count(g)

def count(g):
    safe_place=0
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j]==0:
                safe_place+=1
    return safe_place

loc=[(x,y) for x in range(n) for y in range(m) if not graph[x][y]]

answer=-1

for c in combinations(loc,3):
    g=copy.deepcopy(graph)
    for x,y in c:
        g[x][y]=1
    safe_area=0
    safe_area=max(safe_area, bfs(x,y,g))
    answer=max(answer, safe_area)

print(answer)
