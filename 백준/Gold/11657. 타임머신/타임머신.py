import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
edges = []
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))


def bf(start):
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]

            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost

                # n번째 라운드에서도 값이 갱신된다면 음수 사이클이 존재
                # 이 경우 시작점에서 도달 가능한 음수 사이클이 있다는 뜻
                if i == n - 1:
                    return True  # 음수 사이클 존재
    return False  # 음수 사이클 없음


negative_cycle = bf(1)

if negative_cycle:
    print(-1)
else:
    for d in range(2, n + 1):
        if distance[d] == INF:
            print(-1)
        else:
            print(distance[d])