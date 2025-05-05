import sys
from collections import deque
input=sys.stdin.readline

n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    start,end=map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort()
    graph[end].sort()

visited=[False]*(n+1)
visited[v]=True
def dfs(v):
    print(v, end=' ')
    for node in graph[v]:
        if not visited[node]:
            visited[node]=True
            dfs(node)
    return

dfs(v)
print()

visited=[False]*(n+1)
def bfs(v):
    q=deque()
    q.append(v)
    visited[v] = True
    while q:
        v=q.popleft()
        print(v, end=' ')
        for node in graph[v]:
            if not visited[node]:
                visited[node]=True
                q.append(node)

bfs(v)