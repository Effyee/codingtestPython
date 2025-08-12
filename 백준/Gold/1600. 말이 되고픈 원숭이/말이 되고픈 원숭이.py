import sys
from collections import deque
input = sys.stdin.readline

# 원숭이는 k번 말과 같은 움직임, 이외에는 그냥 인접한 칸으로
# 원숭이가 최소한의 동작으로 시작 지점에서 도착지점까지 갈 수 있는 방법

k = int(input())
w, h = map(int, input().split())

# 0은 평지, 1은 장애물
graph = [list(map(int, input().split())) for _ in range(h)]

# dx, dy 정의: 0~7은 말, 8~11은 일반 이동
horse_dx = [-2, -1, 1, 2, 2, 1, -1, -2]
horse_dy = [-1, -2, -2, -1, 1, 2, 2, 1]
monkey_dx = [0, 0, -1, 1]
monkey_dy = [-1, 1, 0, 0]

visited = [[[False] * (k + 1) for _ in range(w)] for _ in range(h)]

def bfs():
    q = deque()
    # 시작점 (0,0)에 점프 0번 써서 도착. 거리 0
    q.append((0, 0, 0, 0)) # y, x, dist, k_count
    visited[0][0][0] = True

    while q:
        y, x, dist, cnt = q.popleft()

        # 목표 지점 도달 시 거리 반환
        if x == w - 1 and y == h - 1:
            return dist

        # 1. 말처럼 이동 (점프 횟수가 남아있을 때)
        if cnt < k:
            for i in range(8):
                nx = x + horse_dx[i]
                ny = y + horse_dy[i]
                if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] != 1 and not visited[ny][nx][cnt + 1]:
                    visited[ny][nx][cnt + 1] = True
                    q.append((ny, nx, dist + 1, cnt + 1))

        # 2. 인접 칸으로 이동 (항상 가능)
        for i in range(4):
            nx = x + monkey_dx[i]
            ny = y + monkey_dy[i]
            # 범위 체크, 장애물 체크, 방문 여부 체크(중요: cnt 그대로 체크)
            if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] != 1 and not visited[ny][nx][cnt]:
                visited[ny][nx][cnt] = True
                q.append((ny, nx, dist + 1, cnt))

    # 큐가 비었는데 도달 못 한 경우
    return -1

# 시작점이 도착점인 경우 처리
if w == 1 and h == 1:
    print(0)
else:
    print(bfs())