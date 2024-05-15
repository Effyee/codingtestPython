def dfs(x,y,visited):
    if visited[x][y]:
        return False
    visited[x][y]=True

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    if graph[x][y]==0:
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                dfs(nx,ny,visited)


T=int(input())

for _ in range(T):
    N=int(input())

    graph=[list(map(str,input().strip())) for _ in range(N)]
    visited=[[False]*N for _ in range(N)]

    cost=0
    for i in range(N):
        for j in range(N):
            x,y=i,j
            dx = [-1, -1, -1, 0, 0, 1, 1, 1]
            dy = [-1, 0, 1, -1, 1, -1, 0, 1]
            for k in range(8):
                nx=x+dx[k]
                ny=y+dy[k]
                if 0<=nx<N and 0<=ny<N and graph[x][y]=='.':
                    if graph[nx][ny]=='*':
                        cost+=1
            if graph[x][y]=='.':
                graph[x][y]=cost
            cost=0


    answer=0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j]==0:
                dfs(i,j,visited)
                answer+=1

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j]!='*':
                dfs(i,j,visited)
                answer+=1
    print(f'#{_+1} {answer}')
