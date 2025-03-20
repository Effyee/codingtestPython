import sys
from collections import deque

input = sys.stdin.readline
N, M, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 방향: 하 → 우 → 상 → 좌 (반시계)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 회전할 레이어 수
layers = min(N, M) // 2
layer = [deque() for _ in range(layers)]

# 1. 각 레이어를 deque에 저장
for idx in range(layers):
    x, y = idx, idx

    # 하
    for i in range(idx, N - idx - 1):
        layer[idx].append(graph[i][idx])
    # 우
    for i in range(idx, M - idx - 1):
        layer[idx].append(graph[N - idx - 1][i])
    # 상
    for i in range(N - idx - 1, idx, -1):
        layer[idx].append(graph[i][M - idx - 1])
    # 좌
    for i in range(M - idx - 1, idx, -1):
        layer[idx].append(graph[idx][i])

# 2. R번 회전 (deque의 rotate 활용)
for idx in range(layers):
    layer[idx].rotate(R)  # 반시계 방향으로 R번 회전

# 3. 회전된 값을 다시 graph에 반영
for idx in range(layers):
    x, y = idx, idx

    # 하
    for i in range(idx, N - idx - 1):
        graph[i][idx] = layer[idx].popleft()
    # 우
    for i in range(idx, M - idx - 1):
        graph[N - idx - 1][i] = layer[idx].popleft()
    # 상
    for i in range(N - idx - 1, idx, -1):
        graph[i][M - idx - 1] = layer[idx].popleft()
    # 좌
    for i in range(M - idx - 1, idx, -1):
        graph[idx][i] = layer[idx].popleft()

# 4. 결과 출력
for row in graph:
    print(" ".join(map(str, row)))
