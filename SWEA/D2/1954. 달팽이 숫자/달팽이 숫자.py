tc=int(input())

for _ in range(tc):
    n=int(input())

    graph=[[0]*(n) for _ in range(n)]
   
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    x,y=0,-1
    time=1
    dir=0
    while time<=n*n:
        nx = x+dx[dir]
        ny = y+dy[dir]
        if 0<=nx<n and 0<=ny<n and not graph[nx][ny]:
            graph[nx][ny]=time
            x,y=nx,ny
            time += 1
        else:
            if dir==3:
                dir=0
            else:
                dir+=1

    print(f'#{_+1}')
    for i in range(len(graph)):
        print(' '.join(map(str, graph[i])))



