from collections import deque

def bfs(n, k):
    MAX = 100001
    visited = [0] * MAX
    q = deque([n])

    while q:
        x = q.popleft()
        if x == k:
            return visited[x]
        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx < MAX and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                q.append(nx)

# 입력
n, k = map(int, input().split())
print(bfs(n, k))
