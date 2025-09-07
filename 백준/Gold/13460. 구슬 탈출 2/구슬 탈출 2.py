import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[list(input().strip()) for _ in range(n)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]
visited=set()
# 파랑, 빨강 구슬이 같은 칸에 도달하게 되는 순간
# 원래 위치로부터의 거리를 구하고, 길이가 긴게 짤은 것의 뒤로 가도록
def bfs(rx,ry,bx,by):
    q=deque()
    q.append((rx,ry,bx,by,0))
    visited.add((rx,ry,bx,by))
    while q:
        rx,ry,bx,by,dist=q.popleft()
        if dist==10:
            return -1
        for i in range(4):
            nrx,nry,nbx,nby=rx,ry,bx,by
            flag=False
            # 파랑 구슬의 이동
            while True:
                if nbx+dx[i]<0 or nbx+dx[i]>=n or nby+dy[i]<0 or nby+dy[i]>=m or graph[nbx+dx[i]][nby+dy[i]]=='#':
                    break
                nbx += dx[i]
                nby += dy[i]
                if graph[nbx][nby]=='O':
                    flag=True
                    break

            # 파랑 구슬이 구멍에 들어가 버린 경우, 아래를 진행X
            if flag:
                continue

            # 빨강 구슬의 이동
            while True:
                if nrx+dx[i]<0 or nrx+dx[i]>=n or nry+dy[i]<0 or nry+dy[i]>=m or graph[nrx+dx[i]][nry+dy[i]]=='#':
                    break
                nrx += dx[i]
                nry += dy[i]
                # 빨강 구슬이 구멍에 들어간 경우, 바로 답을 반환
                if graph[nrx][nry] == 'O':
                    return dist + 1

            # 둘이 이동을 마치고 난 뒤에, 위치가 같으면 보정
            if (nrx,nry)==(nbx,nby):
                red_dist=abs(nrx-rx)+abs(nry-ry)
                blue_dist=abs(nbx-bx)+abs(nby-by)
                if red_dist>blue_dist:
                    nrx-=dx[i]
                    nry-=dy[i]
                else:
                    nbx-=dx[i]
                    nby-=dy[i]

            # 방문한 적이 없는 경우
            if (nrx,nry,nbx,nby) not in visited:
                visited.add((nrx,nry,nbx,nby))
                q.append((nrx,nry,nbx,nby,dist+1))

    return -1

rx,ry,bx,by=0,0,0,0
for x in range(n):
    for y in range(m):
        if graph[x][y]=='R':
            rx,ry=x,y
        if graph[x][y]=='B':
            bx,by=x,y

answer=bfs(rx,ry,bx,by)
print(answer)
