import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 200001

visited = [int(1e9)] * MAX  # 각 위치에 도달하는 최소 시간
count = 0  # 방법의 수
min_time = int(1e9)  # 최소 시간

def bfs():
    global count, min_time
    q = deque()
    q.append((n, 0))
    visited[n] = 0

    while q:
        now, time = q.popleft()

        if now == k:
            if time < min_time:
                min_time = time
                count = 1
            elif time == min_time:
                count += 1

        for next in (now - 1, now + 1, now * 2):
            if 0 <= next < MAX:
                # 다음 위치를 처음 방문하거나, 같은 시간에 또 도달한 경우
                if visited[next] >= time + 1:
                    visited[next] = time + 1
                    q.append((next, time + 1))

bfs()
print(min_time)
print(count)
