import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)

v,e=map(int,input().split())
distance=[INF]*(v+1)
k=int(input())
graph=[[] for _ in range(v+1)]

for _ in range(e):
    s,e,dist=map(int,input().split())
    graph[s].append([e,dist])

def dijkstra(k):
    hq=[]
    heapq.heappush(hq,(0,k))
    distance[k]=0
    while hq:
        dist,node=heapq.heappop(hq)
        if distance[node]>dist:
            continue
        for next_node,d in graph[node]:
            dd=distance[node]+d
            if distance[next_node]>dd:
                distance[next_node]=dd
                heapq.heappush(hq,(dd,next_node))

    return
dijkstra(k)
for i in range(1,len(distance)):
    if distance[i]==int(1e9):
        print('INF')
    else:
        print(distance[i])