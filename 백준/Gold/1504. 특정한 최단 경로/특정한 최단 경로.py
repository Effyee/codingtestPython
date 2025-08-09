import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))  # 양방향

v1, v2 = map(int, input().split())

def dijkstra(start):
    dist = [INF] * (n + 1)
    dist[start] = 0
    q = [(0, start)]
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for nxt, cost in graph[now]:
            nd = d + cost
            if dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heappush(q, (nd, nxt))
    return dist

dist1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

path1 = dist1[v1] + dist_v1[v2] + dist_v2[n]
path2 = dist1[v2] + dist_v2[v1] + dist_v1[n]

ans = min(path1, path2)
print(ans if ans < INF else -1)
