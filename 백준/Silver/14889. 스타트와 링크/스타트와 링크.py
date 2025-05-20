import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
answer = int(1e9)

def calc_diff():
    start, link = 0, 0
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:
                start += s[i][j]
            elif not visited[i] and not visited[j]:
                link += s[i][j]
    return abs(start - link)

def bt(depth, idx):
    global answer
    if depth == n // 2:
        diff = calc_diff()
        answer = min(answer, diff)
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            bt(depth + 1, i + 1)
            visited[i] = False

bt(0, 0)
print(answer)
