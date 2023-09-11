def dfs(board,m,n,x,y,visited):
    nx,ny=0,0
    visited[x][y]=True
    
    if board[x][y]=='-':
        nx=x
        ny=y+1
    else:
        nx=x+1
        ny=y
    if nx<m and ny<n and board[nx][ny]==board[x][y] and not visited[nx][ny]:
        dfs(board,m,n,nx,ny,visited)
def solution(board,m,n):
    answer=0
    visited=[[False]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if visited[i][j]:
                continue
            dfs(board,m,n,i,j,visited)
            answer+=1
    return answer

if __name__=="__main__":
    m,n=map(int,input().split())
    board=[]
    for _ in range(m):
        row=list(input())
        board.append(row)
    print(solution(board,m,n))