import sys
input = sys.stdin.readline
INF = int(1e9)

# n개의 도시
n = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# m개의 버스
m = int(input())

for _ in range(m):
    start, dest, dist = map(int, input().split())
    if graph[start][dest] > dist:
        graph[start][dest] = dist

for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
