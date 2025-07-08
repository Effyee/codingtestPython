import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False] * 100001
parent = [-1] * 100001

def bfs():
    q = deque()
    q.append((n, 0))
    visited[n] = True
    while q:
        now, cnt = q.popleft()
        if now == k:
            print(cnt)
            path = []
            temp = k
            while temp != -1:
                path.append(temp)
                temp = parent[temp]
            print(' '.join(map(str, path[::-1])))
            break
        for next in (2*now, now-1, now+1):
            if 0 <= next < 100001 and not visited[next]:
                visited[next] = True
                parent[next] = now
                q.append((next, cnt+1))
    return

bfs()
