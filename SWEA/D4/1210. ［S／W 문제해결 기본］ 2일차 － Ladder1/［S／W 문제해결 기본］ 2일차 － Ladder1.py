from collections import deque

def bfs(start_x, start_y):
    q = deque([(start_x, start_y)])
    visited[start_x][start_y] = True


    #오른쪽, 왼쪽이 우선 그리고 위
    dx = [0, 0, -1]
    dy = [1, -1, 0]

    while q:
        x, y = q.popleft()
        if x == 0:  # 가장 위에 도달했을 때, 현재 y 좌표 반환
            return y
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 100 and 0 <= ny < 100 and not visited[nx][ny] and graph[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True
                break
                #여기서 break를 안걸어서 분기를 안걸어주면
    return False

for _ in range(10):
    tc = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    visited = [[False] * 100 for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if graph[i][j] == 2:
                start_x,start_y= i, j

    result = bfs(start_x, start_y)
    print("#{} {}".format(tc, result))
