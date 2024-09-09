from collections import deque

#맵의 크기
n=int(input())

#맵:0, 뱀:1, 사과:2
maps=[[0]*n for _ in range(n)]

#사과 배치
k=int(input())

for _ in range(k):
    x,y=map(int,input().split())
    maps[x-1][y-1]=2

#방향 전환
l=int(input())
info={}

for i in range(l):
    time,direction=input().split()
    info[int(time)]=direction

#방향
#동,남,서,북
dir=0
time=0
dx=[0,1,0,-1]
dy=[1,0,-1,0]
x,y=0,0
snakes=deque([(x,y)])

while True:

    if time in info.keys():
        if info[int(time)]=='D':
            if dir==3:
                dir=0
            else:
                dir+=1
        else:
            if dir==0:
                dir=3
            else:
                dir-=1

    nx=x+dx[dir]
    ny=y+dy[dir]
    time+=1

    if nx<0 or ny<0 or nx>=n or ny>=n or (nx,ny) in snakes:
        print(time)
        break
    if maps[nx][ny]==2:
        snakes.append((nx,ny))
        maps[nx][ny]=1
        x,y=nx,ny
    else:
        snakes.popleft()
        snakes.append((nx, ny))
        maps[x][y]=0
        x, y = nx, ny

