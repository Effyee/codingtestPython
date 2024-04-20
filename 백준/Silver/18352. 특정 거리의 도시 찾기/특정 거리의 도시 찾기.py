import sys
from collections import deque

input=sys.stdin.readline

#도시의 개수 n, 도로의 개수 m, 거리 정보 k 출발 도시 번호 x
n,m,k,x=map(int,input().split())

graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

def bfs(start,k,visited):
    q=deque([(start,0)])
    visited[start]=True
    answer=[]
    while q:
        now, cost = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                if cost+1==k:
                    answer.append(i)
                q.append((i, cost + 1))
                visited[i] = True
    return answer

answer=[]

answer=bfs(x,k,visited)

answer.sort()

if len(answer)==0:
    print(-1)
else:
    for i in answer:
        print(i)



