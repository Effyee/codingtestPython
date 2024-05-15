def dfs(x, y, cnt, start):
    global answer, start_room
    if cnt > answer:
        answer = cnt
        start_room = start
    elif cnt == answer:
        start_room = min(start_room, start)
    visited[x][y] = True
    room_number = graph[x][y]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == room_number + 1:
            dfs(nx, ny, cnt + 1, start)
    visited[x][y] = False

tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    answer = 0
    start_room = n ** 2

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(n):
        for j in range(n):
            dfs(i, j, 1, graph[i][j])

    print(f'#{t} {start_room} {answer}')
