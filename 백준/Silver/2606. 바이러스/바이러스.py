import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(n+1)

def dfs(node):
    visited[node]=True
    for v in graph[node]:
        if not visited[v]:
            dfs(v)
    return

dfs(1)
print(sum(visited) - 1)