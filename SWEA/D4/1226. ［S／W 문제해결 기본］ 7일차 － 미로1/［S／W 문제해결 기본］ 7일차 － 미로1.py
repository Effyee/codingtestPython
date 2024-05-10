from collections import deque
def bfs(x,y):
    q=deque([(x,y)])
    visited[x][y]=True

    dx=[0,0,-1,1]
    dy=[-1,1,0,0]

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<16 and 0<=ny<16 and not visited[nx][ny]:
                if graph[nx][ny]==3:
                    return True

                elif graph[nx][ny]==0:
                    visited[nx][ny]=True
                    q.append((nx,ny))

    return False


for _ in range(10):
    tc=int(input())

    graph=[list(map(int,input().strip())) for _ in range(16)]

    visited=[[False]*16 for _ in range(16)]

    if bfs(1,1):
        print(f'#{_+1} {1}')
    else:
        print(f'#{_+1} {0}')