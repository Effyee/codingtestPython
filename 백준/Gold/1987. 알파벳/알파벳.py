def dfs(x, y, bitmask, cnt):
    global answer
    answer = max(answer, cnt)

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            next_char = ord(graph[nx][ny]) - ord('A')
            if not (bitmask & (1 << next_char)):
                dfs(nx, ny, bitmask | (1 << next_char), cnt + 1)


r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

answer = 0
initial_char = ord(graph[0][0]) - ord('A')
dfs(0, 0, 1 << initial_char, 1)
print(answer)