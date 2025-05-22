import sys
from collections import deque
input = sys.stdin.readline

graph = [list(input().strip()) for _ in range(5)]
answer = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def is_connected(li):
    li_set = set(li)
    start = li[0]  # pop 없이 첫 좌표 고정
    q = deque([start])
    visited = {start}

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if (nx, ny) in li_set and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))
    return len(visited) == 7

def bt(idx, li, s_cnt):
    global answer
    if len(li) == 7:
        if s_cnt >= 4 and is_connected(li):
            answer += 1
        return
    if idx == 25:
        return

    x, y = divmod(idx, 5)
    li.append((x, y))
    bt(idx + 1, li, s_cnt + (1 if graph[x][y] == 'S' else 0))
    li.pop()
    bt(idx + 1, li, s_cnt)

bt(0, [], 0)
print(answer)
