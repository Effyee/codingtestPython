import sys
input=sys.stdin.readline
R,C=map(int,input().split())

graph=[]
for _ in range(R):
    graph.append(list(map(str,input().strip())))

max_length=0

def dfs(x,y,route):
    global max_length
    max_length=max(len(route),max_length)
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<R and 0<=ny<C:
            if graph[nx][ny] not in route:
                dfs(nx,ny,route+graph[nx][ny])

route=graph[0][0]
dfs(0,0,route)

print(max_length)