import sys
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    li = list(map(int, input().split()))
    start_node = li[0]
    idx = 1
    while li[idx] != -1:
        node, dist = li[idx], li[idx + 1]
        graph[start_node].append((node, dist))
        idx += 2


# DFS 함수 정의: start_node에서 가장 먼 노드와 그 거리를 찾는다.
def dfs(start_node, current_dist):
    # 현재 노드로부터 각 노드까지의 거리를 저장할 배열
    # -1로 초기화하여 미방문 상태 표시
    distances = [-1] * (V + 1)
    distances[start_node] = current_dist

    stack = [(start_node, current_dist)]

    farthest_node = start_node
    max_dist = current_dist

    while stack:
        now, dist = stack.pop()

        # 현재까지 찾은 최대 거리보다 더 멀면 갱신
        if dist > max_dist:
            max_dist = dist
            farthest_node = now

        for nxt_node, nxt_dist in graph[now]:
            # 아직 방문하지 않은 노드라면
            if distances[nxt_node] == -1:
                new_dist = dist + nxt_dist
                distances[nxt_node] = new_dist
                stack.append((nxt_node, new_dist))

    return farthest_node, max_dist


# 1. 임의의 점(1번 노드)에서 가장 먼 노드 찾기
farthest_node_from_1, _ = dfs(1, 0)

# 2. 위에서 찾은 노드에서 다시 가장 먼 노드(와 거리) 찾기
# 이 거리가 트리의 지름이 됨
_, diameter = dfs(farthest_node_from_1, 0)

print(diameter)