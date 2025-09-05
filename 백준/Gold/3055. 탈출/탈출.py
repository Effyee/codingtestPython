import sys
from collections import deque
input=sys.stdin.readline

r, c = map(int, input().split())
# 빈 곳 .
# 물이 찬 지역 *
# 굴 D
# 고슴도치 위치 S
# 돌 X

graph=[list(input().strip()) for _ in range(r)]
visited=[[False]*c for _ in range(r)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(q):
    while q:
        who,x,y,cnt=q.popleft()
        if who=='S' and graph[x][y]=='D':
            return cnt
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if who=='*':
                    if graph[nx][ny]=='.':
                        graph[nx][ny]='*'
                        q.append(('*',nx,ny,cnt+1))
                else:
                    if not visited[nx][ny] and graph[nx][ny]=='.' or graph[nx][ny]=='D':
                        visited[nx][ny]=True
                        q.append(('S',nx,ny,cnt+1))

    return 'KAKTUS'

x,y=0,0
q=deque()
for i in range(r):
    for j in range(c):
        if graph[i][j]=='*':
            q.append(('*',i,j,0))
        elif graph[i][j]=='S':
            x,y=i,j
q.append(('S',x,y,0))
visited[x][y]=True

answer=bfs(q)
print(answer)