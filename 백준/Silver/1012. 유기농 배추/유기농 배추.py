import sys
from collections import deque
input=sys.stdin.readline

def bfs(x, y):
    q = deque([[x, y]])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:  
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])


T=int(input())

for _ in range(T):
    M, N, K = map(int, input().split())  
    graph = [[0]*M for _ in range(N)]   
    visited = [[False]*M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1 

    answer = 0
    for i in range(N):        
        for j in range(M):    
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                answer += 1
    print(answer)
