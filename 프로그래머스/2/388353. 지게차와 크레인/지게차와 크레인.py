from collections import deque

def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    # 패딩 + 내부를 리스트로
    board = [[0] * (m + 2)]
    for row in storage:
        board.append([0] + list(row) + [0])
    board.append([0] * (m + 2))

    def forklift(ch):
        q = deque()
        visited = [[False] * (m + 2) for _ in range(n + 2)]
        q.append((0, 0))
        visited[0][0] = True
        # 바깥 빈 공간을 BFS
        while q:
            x, y = q.popleft()
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n+2 and 0 <= ny < m+2 and not visited[nx][ny]:
                    if board[nx][ny] == 0:
                        visited[nx][ny] = True
                        q.append((nx, ny))
        # 방문한 빈 칸과 인접한 ch 제거
        to_remove = []
        for x in range(1, n+1):
            for y in range(1, m+1):
                if board[x][y] == ch:
                    # 인접 4방 중 하나라도 visited 빈칸이면 제거 대상
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x + dx, y + dy
                        if visited[nx][ny]:
                            to_remove.append((x, y))
                            break
        for x, y in to_remove:
            board[x][y] = 0

    def crane(ch):
        for i in range(1, n+1):
            for j in range(1, m+1):
                if board[i][j] == ch:
                    board[i][j] = 0

    for req in requests:
        if len(req) == 1:
            forklift(req[0])
        else:
            crane(req[0])

    # 남은 컨테이너 수
    ans = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if board[i][j] != 0:
                ans += 1
    return ans
