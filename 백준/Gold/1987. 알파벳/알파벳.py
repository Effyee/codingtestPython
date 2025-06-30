import sys
input=sys.stdin.readline

r,c=map(int,input().split())
graph=[list(input().rstrip()) for _ in range(r)]

visited=[False]*(26)
answer=0

def dfs(x,y,cnt):
    global answer
    answer=max(answer,cnt)
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<r and 0<=ny<c:
            idx=ord(graph[nx][ny])-ord('A')
            if not visited[idx]:
                visited[idx] = True
                dfs(nx, ny, cnt + 1)
                visited[idx] = False

visited[ord(graph[0][0])-ord('A')]=True
dfs(0,0,1)
print(answer)