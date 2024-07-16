import sys
from collections import deque

input=sys.stdin.readline

n,m,k,x=map(int,input().split())
visited=[False]*(n+1)
answer=[]
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

def bfs(start):
    q=deque([(start,0)])
    visited[start]=True

    while q:
        now,dist=q.popleft()
        if dist==k:
            answer.append(now)
        for node in graph[now]:
            if not visited[node]:
                visited[node]=True
                q.append((node,dist+1))

bfs(x)

if answer:
    answer.sort()
    for a in answer:
        print(a)
else:
    print(-1)