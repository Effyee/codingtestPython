import sys
from collections import deque
input=sys.stdin.readline

k=int(input())
# 열, 행
w,h=map(int,input().split())
visited=[[[False]*(k+1) for _ in range(w)] for _ in range(h)]
graph=[list(map(int,input().split())) for _ in range(h)]

# 말 이동 (행, 열)
dhx=[-2,-1,1,2,2,1,-1,-2]
dhy=[-1,-2,-2,-1,1,2,2,1]

# 원숭이 이동
dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs():
    q=deque()
    # 행, 열
    # x,y, 말 이동 횟수, 거리
    q.append((0,0,0,0))
    # 말 이동을 사용 하지 않고 도달한 곳 [][][0]
    # 말 이동 한 번 이용 후 도달 [][][1]
    visited[0][0][0]=True
    while q:
        x,y,cnt,dist=q.popleft()
        if x==h-1 and y==w-1:
            return dist
        if cnt<k:
            for i in range(8):
                nx=x+dhx[i]
                ny=y+dhy[i]
                if 0<=nx<h and 0<=ny<w:
                    if not visited[nx][ny][cnt+1] and graph[nx][ny]!=1:
                        visited[nx][ny][cnt+1]=True
                        q.append((nx,ny,cnt+1,dist+1))
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx <h and 0 <= ny <w:
                if not visited[nx][ny][cnt] and graph[nx][ny] != 1:
                    visited[nx][ny][cnt]=True
                    q.append((nx,ny,cnt,dist+1))

    return -1

print(bfs())