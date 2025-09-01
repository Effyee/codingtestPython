from collections import defaultdict, deque
import sys
input=sys.stdin.readline

n=int(input())
graph=[[0]*n for _ in range(n)]

k=int(input())
for _ in range(k):
    x,y=map(int,input().split())
    graph[x-1][y-1]=1

l=int(input())
d=defaultdict(int)
for _ in range(l):
    x,c=input().split()
    d[int(x)]=c

dx=[0,1,0,-1]  # 오른쪽, 아래, 왼쪽, 위
dy=[1,0,-1,0]

direction=0
time=0
snake=deque()
snake.append((0,0))

while True:
    x,y=snake[-1]   # 머리 좌표
    nx,ny=x+dx[direction], y+dy[direction]

    # 벽이나 자기 몸에 부딪힘
    if not (0<=nx<n and 0<=ny<n) or (nx,ny) in snake:
        print(time+1)
        break

    # 머리 이동
    snake.append((nx,ny))
    if graph[nx][ny]==1:   # 사과 있음
        graph[nx][ny]=0
    else:                  # 사과 없음 → 꼬리 제거
        snake.popleft()

    # 방향 전환
    if time+1 in d:
        if d[time+1]=='L':
            direction=(direction-1)%4
        else:
            direction=(direction+1)%4

    time+=1
