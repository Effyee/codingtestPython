import heapq

INF = int(1e9)


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]

    for start, dest in edge:
        graph[start].append(dest)  # start에서 dest로 가는 간선 추가
        graph[dest].append(start)  # dest에서 start로 가는 간선 추가 (양방향)

    distance = dijkstra(n, graph)

    # 최댓값을 찾아 그 노드의 개수를 센다
    max_distance = max(distance[1:])  # 0번 인덱스는 사용하지 않음
    answer = distance.count(max_distance)  # 가장 멀리 있는 노드의 개수

    return answer


def dijkstra(n, graph):
    distance = [INF] * (n + 1)
    distance[1] = 0  # 시작 노드의 거리는 0
    q = []
    heapq.heappush(q, (0, 1))  # (거리, 노드)

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for v in graph[now]:  # 연결된 노드
            cost = dist + 1  # 모든 간선의 가중치는 1
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

    return distance

