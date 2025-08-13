import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)
# n 명의 학생, m개의 도로, 도착지 x
n,m,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
reversed_graph=[[] for _ in range(n+1)]

# 학생-> 목표지점
# 각 학생 집에서 목표 지점까지 dijkstra 돌리면
# 너무 많이 걸리기 때문에 길을 반대로해서 구하고,
# 목표지점-> 각 집
# 그냥 목표지점에서 dijkstra 돌리면 된다.

for _ in range(m):
    start,end,dist=map(int,input().split())
    graph[start].append((end,dist))
    reversed_graph[end].append((start,dist))



def dijkstra(start,graph):
    distance = [INF] * (n + 1)
    hq=[]
    heapq.heappush(hq,(0,start))
    distance[start]=0

    while hq:
        d,now=heapq.heappop(hq)
        if d>distance[now]:
            continue
        for nxt,cost in graph[now]:
            dist=cost+d
            if distance[nxt]>dist:
                distance[nxt]=dist
                heapq.heappush(hq,(dist,nxt))
    return distance

d1=dijkstra(x,reversed_graph)
d2=dijkstra(x,graph)

answer=-int(1e9)
for i in range(1,n+1):
    answer=max(answer,d1[i]+d2[i])

print(answer)