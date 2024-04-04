import sys
from collections import deque

#도시의 개수, 도로의 개수, 거리정보, 출발 도시 번호
n,m,k,x=map(int,sys.stdin.readline().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)


vistied=[False]*(n+1)
distance=[[] for _ in range(n+1)]

def bfs(graph,start,visited):
    q=deque()
    q.append((start,0))
    visited[start]=True

    while q:
        v,dist=q.popleft()
        distance[v]=dist
        for i in graph[v]:
            if not visited[i]:
                q.append((i,dist+1))
                visited[i]=True




bfs(graph,x,vistied)

for i in range(n+1):
    if distance[i]==k:
        print(i)
        
if k not in distance:
    print(-1)
