from collections import deque, defaultdict

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False]*m for _ in range(n)]

    cluster_id = 1
    coords = {}            # (x,y) -> cluster_id
    oil_size = {}          # cluster_id -> 덩어리 크기
    cols_in_cluster = defaultdict(set)  # cluster_id -> 덩어리가 포함된 열

    def bfs(sx, sy, cid):
        q = deque([(sx, sy)])
        visited[sx][sy] = True
        coords[(sx, sy)] = cid
        size = 1
        cols = {sy}

        while q:
            x, y = q.popleft()
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and land[nx][ny] == 1:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        coords[(nx, ny)] = cid
                        size += 1
                        cols.add(ny)
        oil_size[cid] = size
        cols_in_cluster[cid] = cols
    
    # cluster labeling
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j, cluster_id)
                cluster_id += 1

    #열별 석유량
    col_score = [0]*m
    for cid, cols in cols_in_cluster.items():
        for c in cols:
            col_score[c] += oil_size[cid]
    return max(col_score)
    