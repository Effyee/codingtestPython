import sys
from collections import deque
input=sys.stdin.readline

"""
1. 하얀색: 배양액X->1
2. 황토색: 배양액O->2
3. 하늘색: 호수->0
# 동일 시간에 도달, 꽃이 핌
"""
n,m,g,r=map(int,input().split())
garden=[list(map(int,input().split())) for _ in range(n)]

answer = 0

def choose_RG(gc, rc, li, start, coords):
    global answer
    if gc == g and rc == r:
        visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
        q = deque()
        for color, x, y in li:
            visited[x][y] = [color, 0]
            q.append((color, x, y, 0))

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        result = 0

        while q:
            color, x, y, cnt = q.popleft()
            if visited[x][y][0] == 'f':  # 꽃이면 확산 중단
                continue
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    # 배양액 가능한 땅(황토색)이고 아직 방문 X
                    if visited[nx][ny][0] == 0 and (garden[nx][ny] == 1 or garden[nx][ny] == 2):
                        visited[nx][ny] = [color, cnt+1]
                        q.append((color, nx, ny, cnt+1))
                    # 다른 색과 동시에 도착 → 꽃
                    elif color == 'r' and visited[nx][ny][0] == 'g' and visited[nx][ny][1] == cnt+1:
                        visited[nx][ny] = ['f', cnt+1]
                        result += 1
                    elif color == 'g' and visited[nx][ny][0] == 'r' and visited[nx][ny][1] == cnt+1:
                        visited[nx][ny] = ['f', cnt+1]
                        result += 1

        answer = max(answer, result)
        return

    if gc > g or rc > r:
        return

    for i in range(start, len(coords)):
        choose_RG(gc+1, rc, li+[('g', coords[i][0], coords[i][1])], i+1, coords)
        choose_RG(gc, rc+1, li+[('r', coords[i][0], coords[i][1])], i+1, coords)


def choose_XY(n,m,k,choosen,idx):
    if len(choosen) == k:
        coords=[divmod(c,m) for c in choosen]
        choose_RG(0,0,[],0,coords)
        return
    for i in range(idx, n*m):
        x, y = divmod(i, m)
        if garden[x][y] == 2:  # 황토색 땅만 선택
            choose_XY(n,m,k,choosen+[i],i+1)
    return


choose_XY(n,m,g+r,[],0)
print(answer)
