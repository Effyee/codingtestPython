from collections import deque

def bfs(maps, visited):
    q = deque([(0, 0, 0)])
    visited[0][0] = True

    while q:
        x, y, dist = q.popleft()
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        
        # 목표 도달 시
        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            return dist + 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[nx][ny] != 0:
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))

    return -1  # 경로가 없을 경우 -1 반환


def solution(maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    answer = bfs(maps, visited)
    return answer  # 경로가 없으면 -1이 반환됨