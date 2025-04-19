import sys
from collections import deque
input = sys.stdin.readline

graph = [list(input().strip()) for _ in range(5)]
candidates = [(x, y) for x in range(5) for y in range(5)]
answer = []

def check(li):
    cnt = sum(1 for x, y in li if graph[x][y] == 'S')
    if cnt < 4:
        return False

    visited = set()
    q = deque([li[0]])
    visited.add(li[0])
    li_set = set(li)

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in li_set and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))

    return len(visited) == 7

def backtrack(idx, li):
    if len(li) == 7:
        if check(li):
            answer.append(li)
        return
    if idx == 25:
        return

    backtrack(idx + 1, li + [candidates[idx]])
    backtrack(idx + 1, li)

backtrack(0, [])
print(len(answer))
