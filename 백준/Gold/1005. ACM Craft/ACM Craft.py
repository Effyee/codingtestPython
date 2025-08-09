import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    costs = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for _ in range(k):
        start, end = map(int, input().split())
        graph[start].append(end)
        indegree[end] += 1
    dp = [0] * (n + 1)
    target = int(input())

    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            dp[i] = costs[i]
            q.append(i)

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            dp[nxt] = max(dp[nxt], dp[now] + costs[nxt])
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    print(dp[target])
