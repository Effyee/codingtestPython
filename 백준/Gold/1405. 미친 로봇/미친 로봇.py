def dfs(x, y, n, prob):
    if visited[x][y]: return 0  # 이미 방문한 위치면 단순하지 않은 경로
    if n == 0: return prob  # 모든 이동을 마쳤으면 현재 확률을 반환

    visited[x][y] = True  # 현재 위치 방문 처리

    # 동서남북 방향으로 이동
    ret = 0
    ret += dfs(x, y + 1, n - 1, prob * probs[0])
    ret += dfs(x, y - 1, n - 1, prob * probs[1])
    ret += dfs(x + 1, y, n - 1, prob * probs[2])
    ret += dfs(x - 1, y, n - 1, prob * probs[3])

    visited[x][y] = False  #백트래킹

    return ret


N, e, w, s, n = map(int, input().split())
probs = [e / 100, w / 100, s / 100, n / 100]  
visited = [[False] * 29 for _ in range(29)]

print(dfs(14, 14, N, 1))