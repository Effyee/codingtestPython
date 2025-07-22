import sys
from collections import deque, defaultdict

# 표준 입력을 더 빠르게 읽기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 테스트 케이스의 개수: k
k = int(input())


# BFS를 사용하여 특정 컴포넌트가 이분 그래프인지 판별하는 함수
# start_node: BFS 탐색을 시작할 노드
# graph: 그래프의 인접 리스트
# color: 각 노드의 색깔을 저장하는 리스트 (0: 미방문, 1: 첫 번째 색, 2: 두 번째 색)
def bfs(start_node, graph, color):
    q = deque([start_node])
    # 시작 노드의 색깔은 이미 외부에서 1로 칠해져 있다고 가정

    while q:
        now = q.popleft()  # 현재 탐색할 노드

        # 현재 노드의 색깔을 기반으로 다음 이웃 노드의 색깔을 결정
        # 현재 노드가 1이면 다음 노드는 2, 현재 노드가 2이면 다음 노드는 1
        next_color = 2 if color[now] == 1 else 1

        # 현재 노드의 모든 이웃 노드들을 탐색
        for neighbor in graph[now]:
            if not color[neighbor]:  # 아직 색칠되지 않은 이웃 노드라면
                color[neighbor] = next_color  # 결정된 색깔로 칠하고
                q.append(neighbor)  # 큐에 추가하여 다음 탐색 대상으로 만듦
            elif color[neighbor] == color[now]:  # 이미 색칠된 이웃 노드인데, 현재 노드와 같은 색이라면
                # 이는 이분 그래프의 정의에 위배되므로 모순 발생
                return False  # 이분 그래프가 아님을 반환
            # else: color[neighbor] != color[now]
            # 이웃 노드가 이미 다른 색으로 칠해져 있다면, 이는 이분 그래프 조건에 부합하므로 문제 없음

    return True  # 현재 컴포넌트는 성공적으로 이분 그래프 조건을 만족함


# 각 테스트 케이스를 처리하는 루프
for _ in range(k):
    # 그래프 정점의 개수 V, 간선의 개수 E
    v, e = map(int, input().split())

    # 각 노드의 색깔을 저장할 리스트 초기화
    # 0: 아직 방문하지 않음, 1: 첫 번째 그룹, 2: 두 번째 그룹
    color = [0] * (v + 1)

    # 그래프의 인접 리스트를 defaultdict를 사용하여 초기화
    graph = defaultdict(list)

    # 간선 정보 입력 (양방향 그래프)
    for _ in range(e):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    # 현재 테스트 케이스의 이분 그래프 여부를 나타내는 플래그
    is_bipartite = True

    # 모든 노드를 순회하며 연결되지 않은 컴포넌트도 처리
    for i in range(1, v + 1):
        if not color[i]:  # 아직 방문하지 않은 노드라면 (새로운 컴포넌트의 시작)
            color[i] = 1  # 첫 번째 색깔(1)로 시작 노드를 칠함
            # BFS를 실행하여 이 컴포넌트가 이분 그래프인지 확인
            if not bfs(i, graph, color):
                is_bipartite = False  # 이분 그래프가 아님을 표시
                break  # 이미 이분 그래프가 아님이 확인되었으므로 더 이상 확인할 필요 없음

    if is_bipartite:
        print("YES")
    else:
        print("NO")