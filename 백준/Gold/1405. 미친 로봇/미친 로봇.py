def dfs(x, y, ref, cnt):
    if visited[x][y]:
        return
    if cnt == time:
        global possibility
        possibility += ref
        return

    visited[x][y] = True

    dfs(x, y+1, ref*p[0], cnt+1)
    dfs(x, y-1, ref*p[1], cnt+1)
    dfs(x+1, y, ref*p[2], cnt+1)
    dfs(x-1, y, ref*p[3], cnt+1)

    visited[x][y] = False  # 방문 상태를 원래대로 되돌림


time, e, w, s, n = map(int, input().split())
p = [e/100, w/100, s/100, n/100]
visited = [[False]*29 for _ in range(29)]
possibility = 0
dfs(14, 14, 1, 0)  # 시작 위치 (14, 14)는 가운데 위치를 의미
print(possibility)