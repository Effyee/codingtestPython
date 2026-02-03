import sys
input=sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
graph=[list(map(str,input().rstrip())) for _ in range(n)]
visited=set()
def bfs(rx,ry,bx,by):
    q=deque()
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    q.append((rx,ry,bx,by,0))
    visited.add((rx,ry,bx,by))

    while q:
        rx,ry,bx,by,count=q.popleft()
        if count==10:
            return -1

        for i in range(4):
            nrx, nry, nbx, nby = rx, ry, bx, by
            flag=False
            while True:
                if nbx+dx[i]<0 or nbx+dx[i]>=n or nby+dy[i]<0 or nby+dy[i]>=m or graph[nbx+dx[i]][nby+dy[i]]=='#':
                    break
                nbx+=dx[i]
                nby+=dy[i]
                if graph[nbx][nby]=='O':
                    flag=True
                    break

            if flag:
                continue

            while True:
                if nrx+dx[i]<0 or nrx+dx[i]>=n or nry+dy[i]<0 or nry+dy[i]>=m or graph[nrx+dx[i]][nry+dy[i]]=='#':
                    break
                nrx+=dx[i]
                nry+=dy[i]
                if graph[nrx][nry]=='O':
                    return count+1

            if (nrx,nry)==(nbx,nby):
                red_dist=abs(nrx-rx)+abs(nry-ry)
                blue_dist=abs(nbx-bx)+abs(nby-by)
                if red_dist>blue_dist:
                    nrx-=dx[i]
                    nry-=dy[i]
                else:
                    nbx-=dx[i]
                    nby-=dy[i]

            if (nrx,nry,nbx,nby) not in visited:
                visited.add((nrx,nry,nbx,nby))
                q.append((nrx,nry,nbx,nby,count+1))
    return -1

rx,ry,bx,by=0,0,0,0
for i in range(n):
    for j in range(m):
        if graph[i][j]=='R':
            rx,ry=i,j
        elif graph[i][j]=='B':
            bx,by=i,j

answer=bfs(rx,ry,bx,by)
print(answer)