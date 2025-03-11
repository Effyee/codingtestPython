import sys

input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

# 간선 정보 입력 (M번 반복)
for _ in range(M):
    arr, des = map(int, input().split())
    graph[arr].append(des)
    graph[des].append(arr)

# 작은 숫자부터 방문하도록 정렬
for i in range(1, N + 1):
    graph[i].sort()

visited = [False] * (N + 1)


# DFS 구현
def dfs(now, visited):
    print(now, end=' ')  # 첫 방문 노드 출력
    visited[now] = True
    for i in graph[now]:
        if not visited[i]:
            dfs(i, visited)


visited = [False] * (N + 1) 
dfs(V, visited)
print()  


# BFS 구현
def bfs(start, visited):
    q = deque([start])
    visited[start] = True  

    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True  
                q.append(i)


visited = [False] * (N + 1)  
bfs(V, visited)