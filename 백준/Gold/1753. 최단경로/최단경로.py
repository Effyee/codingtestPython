import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)
v,e=map(int,input().split())
#시작 정점 번호
k=int(input())
graph=[[] for _ in range(v+1)]
for _ in range(e):
    start,end,w=map(int,input().split())
    graph[start].append((end,w))

distances=[INF]*(v+1)
def dijkstra(start):
    hq=[]
    heapq.heappush(hq,(0,start))
    distances[start]=0
    while hq:
        dist,now=heapq.heappop(hq)
        if distances[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distances[i[0]]:
                distances[i[0]]=cost
                heapq.heappush(hq,(cost,i[0]))

dijkstra(k)
for i in range(1, v+1):
    if distances[i] == INF:
        print("INF")
    else:
        print(distances[i])
