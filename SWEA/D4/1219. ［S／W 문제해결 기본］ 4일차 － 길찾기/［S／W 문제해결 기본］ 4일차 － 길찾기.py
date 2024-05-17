def dfs(graph, node, visited):
    if node == 99:
        return True
    visited[node] = True
    for n in graph[node]:
        if not visited[n]:
            if dfs(graph, n, visited):  # 재귀 호출에서 True를 반환받은 경우
                return True  # 상위 호출로 True를 반환
    return False  # 목표 노드에 도달하지 못했으면 False 반환

for _ in range(10):
    tc, n = map(int, input().split())
    graph = [[] for _ in range(100)]
    visited = [False] * 100

    road=list(map(int,input().split()))

    for i in range(0,len(road)-1,2):
        start=road[i]
        end=road[i+1]
        graph[start].append(end)

    if dfs(graph, 0, visited):
        print(f'#{_+1} {1}')
    else:
        print(f'#{_+1} {0}')  # dfs 함수에서 False를 반환한 경우 0을 출력