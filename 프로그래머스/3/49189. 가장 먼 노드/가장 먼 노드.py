from collections import deque
INF=int(1e9)
def bfs(start,distance,graph):
    q=deque([(start)])
    distance[start]=0

    while q:
        now=q.popleft()
        for v in graph[now]:
            if distance[v]==INF:
                distance[v]=distance[now]+1
                q.append(v)
    return distance


def solution(n, edge):
    graph=[[] for _ in range(n+1)]
    distance=[INF]*(n+1)
    distance[0]=0
    for e in edge:
        start,end=e
        graph[start].append(end)
        graph[end].append(start)

    print(bfs(1,distance,graph))
    m=max(distance)

    return distance.count(m)