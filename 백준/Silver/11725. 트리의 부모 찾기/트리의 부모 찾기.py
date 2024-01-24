import sys
from collections import deque

n=int(sys.stdin.readline().rstrip())
graph=[[] for i in range(n+1)]

for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


visited=[False]*(n+1)

answer=[]
def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                answer.append((v,i))
                visited[i]=True

bfs(graph,1,visited)
answer=sorted(answer, key=lambda x: x[1])

for i in range(len(answer)):
    print(answer[i][0])
