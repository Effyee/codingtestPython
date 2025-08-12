import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)

# n개의 마을, m개의 단방향 도로, x번 마을에서 파티
n, m, x = map(int, input().split())

# 원래 그래프와 역방향 그래프를 함께 생성
graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    # 시작점, 끝점, 소요 시간
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    reverse_graph[end].append((start, cost))

def dijkstra(start, graph_to_search):
    # 각 실행마다 새로운 distance 배열을 만들어야 함
    distance = [INF] * (n + 1)
    q = []
    
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for nxt, cost in graph_to_search[now]:
            d = cost + dist
            if d < distance[nxt]:
                distance[nxt] = d
                heapq.heappush(q, (d, nxt))
    return distance # 결과 배열을 반환

# 1. 파티에 '가는' 최단 시간 계산 (역방향 그래프 이용)
go_to_party = dijkstra(x, reverse_graph)

# 2. 파티에서 '돌아오는' 최단 시간 계산 (원래 그래프 이용)
return_home = dijkstra(x, graph)

# 3. 왕복 시간 계산 및 최댓값 찾기
max_time = 0
for i in range(1, n + 1):
    round_trip_time = go_to_party[i] + return_home[i]
    if round_trip_time > max_time:
        max_time = round_trip_time

print(max_time)