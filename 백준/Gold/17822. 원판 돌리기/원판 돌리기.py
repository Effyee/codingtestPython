import sys
from collections import deque
input = sys.stdin.readline

N, M, T = map(int, input().split())
arr = [deque(map(int, input().split())) for _ in range(N)]

# BFS로 같은 인접 수 찾기
def bfs(i, j, visited):
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    value = arr[i][j]
    same = [(i, j)]

    while q:
        x, y = q.popleft()
        
        # 상하좌우
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx = x + dx
            ny = (y + dy) % M   # 원형 처리

            if 0 <= nx < N and not visited[nx][ny] and arr[nx][ny] == value:
                visited[nx][ny] = True
                q.append((nx, ny))
                same.append((nx, ny))

    return same


for _ in range(T):
    x, d, k = map(int, input().split())

    # 1. 회전
    for i in range(x-1, N, x):
        if d == 0:      # 시계
            arr[i].rotate(k)
        else:           # 반시계
            arr[i].rotate(-k)

    # 2. 인접하면서 같은 수 찾기
    visited = [[False] * M for _ in range(N)]
    to_remove = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and not visited[i][j]:
                same = bfs(i, j, visited)
                if len(same) > 1:
                    to_remove.extend(same)

    # 3. 지울 것이 있다면 지움
    if to_remove:
        for i, j in to_remove:
            arr[i][j] = 0
    else:
        # 4. 평균 계산 후 조정
        total = 0
        count = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] > 0:
                    total += arr[i][j]
                    count += 1

        if count > 0:
            avg = total / count
            for i in range(N):
                for j in range(M):
                    if arr[i][j] > 0:
                        if arr[i][j] > avg:
                            arr[i][j] -= 1
                        elif arr[i][j] < avg:
                            arr[i][j] += 1

# 5. 최종 합 출력
answer = sum(sum(row) for row in arr)
print(answer)
