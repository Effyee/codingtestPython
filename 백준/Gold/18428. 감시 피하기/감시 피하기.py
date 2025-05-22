import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
school=[list(map(str,input().rsplit())) for _ in range(n)]

def bfs(walls):

    for x,y in walls:
        school[x][y]='O'
    q=deque([])
    for i in range(n):
        for j in range(n):
            if school[i][j]=='T':
                q.append([i,j])
    #왼,오,위,아래
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x,y
            while True:
                nx+=dx[i]
                ny+=dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if school[nx][ny]=='S':
                        for x,y in walls:
                            school[x][y]='X'
                        return False
                    if school[nx][ny]=='O':
                        break
                else:
                    break
    for x, y in walls:
        school[x][y] = 'X'
    return True

def bt(li,idx):
    if len(li)==3:
        if bfs(li):
            print('YES')
            exit()
        return
    if idx==n*n:
        return

    x,y=divmod(idx,n)
    if school[x][y]=='X':
        li.append([x,y])
        bt(li,idx+1)
        li.pop()
    bt(li,idx+1)
    return

bt([],0)
print('NO')