from collections import deque

def bfs():
    answer = set()
    q = deque([])

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        for j in range(4):
            q.append((i, j, graph[i][j]))

    while q:
        x, y, s = q.popleft()
        if len(s) == 7:
            answer.add(s)
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                new_s = s + graph[nx][ny]
                q.append((nx, ny, new_s))

    return len(answer)

T = int(input())

for _ in range(T):
    graph = [list(input().split()) for _ in range(4)]

    answer = bfs()

    print(f'#{_+1} {answer}')