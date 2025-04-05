import sys
from collections import deque

input=sys.stdin.readline

M,N,H=map(int,input().split())

rec=[]

for _ in range(H):
    floor=[]
    for _ in range(N):
        floor.append(list(map(int,input().split())))
    rec.append(floor)
d=-1
def bfs():
    global d
    q=deque()
    for h in range(H):
        for x in range(N):
            for y in range(M):
                if rec[h][x][y]==1:
                    q.append([0,h,x,y])
    while q:
        day,h,x,y=q.popleft()
        d=max(d,day)
        # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
        dh=[-1,1,0,0,0,0]
        dx=[0,0,-1,1,0,0]
        dy=[0,0,0,0,-1,1]
        for i in range(6):
            nh=h+dh[i]
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nh<H and 0<=nx<N and 0<=ny<M:
                if rec[nh][nx][ny]==0:
                    rec[nh][nx][ny]=1
                    q.append([day+1,nh,nx,ny])

bfs()
for h in range(H):
    for x in range(N):
        for y in range(M):
            if rec[h][x][y] == 0:
                print(-1)
                exit()

print(d)