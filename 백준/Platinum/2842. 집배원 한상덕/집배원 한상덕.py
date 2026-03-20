import sys
from collections import deque
input = sys.stdin.readline

# 입력
n = int(input())
graph = [list(input().strip()) for _ in range(n)]
cost = [list(map(int, input().split())) for _ in range(n)]

# 시작점(P), 집(K) 개수 찾기
home = 0
sx, sy = 0, 0
heights = set()

for i in range(n):
    for j in range(n):
        heights.add(cost[i][j])
        if graph[i][j] == 'K':
            home += 1
        elif graph[i][j] == 'P':
            sx, sy = i, j

heights = sorted(heights)

# 8방향
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

# BFS
def bfs(low, high):
    # 시작점이 범위 밖이면 불가능
    if not (low <= cost[sx][sy] <= high):
        return False

    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True

    count = 0

    while q:
        x, y = q.popleft()

        if graph[x][y] == 'K':
            count += 1

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if low <= cost[nx][ny] <= high:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return count == home


# 투 포인터
answer = int(1e9)
left = 0
right = 0

while left < len(heights):
    while right < len(heights):
        if bfs(heights[left], heights[right]):
            answer = min(answer, heights[right] - heights[left])
            break
        right += 1
    left += 1

print(answer)