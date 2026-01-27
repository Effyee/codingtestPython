from collections import defaultdict, deque

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False]*m for _ in range(n)]
    # oil_size[oil_id]=해당 오일 덩어리 크기
    # column_oils[행 번호]=oil_id
    oil_size = dict()              # oil_id -> 덩어리 크기
    column_oils = defaultdict(set) # col -> 포함된 oil_id
    oil_id = 0

    def bfs(x, y):
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        q = deque()
        q.append((x, y))
        visited[x][y] = True

        count = 1
        cols = {y}   # ⭐ 이 덩어리가 포함하는 열들

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and land[nx][ny] == 1:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        count += 1
                        cols.add(ny)

        return count, cols

    # 1️⃣ 모든 오일 덩어리 분리
    for x in range(n):
        for y in range(m):
            if land[x][y] == 1 and not visited[x][y]:
                count, cols = bfs(x, y)
                oil_size[oil_id] = count
                for col in cols:
                    column_oils[col].add(oil_id)
                oil_id += 1

    # 2️⃣ 열별 시추 결과 계산
    answer = 0
    for col in range(m):
        total = 0
        for oid in column_oils[col]:
            total += oil_size[oid]
        answer = max(answer, total)
    # print(oil_size)
    # print(column_oils)
    return answer
