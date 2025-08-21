import heapq
def solution(n, edge):
    answer = 1
    graph=[[] for _ in range(n+1)]
    for s,e in edge:
        graph[s].append((e,1))
        graph[e].append((s,1))

    def dijkstra(start):
        INF=int(1e9)
        distance=[INF]*(n+1)
        hq=[]
        heapq.heappush(hq,(0,start))
        distance[start]=0
        while hq:
            dist,now=heapq.heappop(hq)
            if distance[now]<dist:
                continue
            for nxt,d in graph[now]:
                cost=d+dist
                if distance[nxt]>cost:
                    distance[nxt]=cost
                    heapq.heappush(hq,(cost,nxt))
        return distance
    
    distance=dijkstra(1)
    m=-int(1e9)
    print(distance)
    for i in range(2,n+1):
        if distance[i]>m:
            m=max(m,distance[i])
            answer=1
        elif distance[i]==m:
            answer+=1
        
    return answer