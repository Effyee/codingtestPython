import sys
INF=int(1e9)
input=sys.stdin.readline

n=int(input())
m=int(input())

graph=[[INF]*(n) for _ in range(n)]

for _ in range(m):
    start,des,cost=map(int,input().split())
    if graph[start-1][des-1]>cost:
        graph[start-1][des-1]=cost

for i in range(n):
    graph[i][i]=0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
for i in range(n):
    for j in range(n):
        if graph[i][j]==INF:
            graph[i][j]=0

for i in range(n):
    s=' '.join(map(str,graph[i]))
    print(s)

