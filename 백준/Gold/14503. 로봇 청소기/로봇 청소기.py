import sys
input=sys.stdin.readline

N,M=map(int,input().split())
r,c,d=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]
visited=[[False]*M for _ in range(N)]

def check(direction, x, y, visited):
    # 북(0) 서(3) 남(2) 동(1) 순서로 왼쪽부터 탐색
    dx = [-1, 0, 1, 0]  # 북 동 남 서
    dy = [0, 1, 0, -1]
    for i in range(4):
        direction = (direction + 3) % 4  # 왼쪽 회전
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 0:
            return direction, nx, ny
    return -1, -1, -1  # 청소할 곳이 없음

def solution(r,c,d,visited):
    answer=0
    #시작 칸 청소
    if graph[r][c]==0 and not visited[r][c]:
        answer+=1
        visited[r][c]=True

    while True:
        direction,x,y=check(d,r,c,visited)
        #청소할 곳이 없음
        if direction == -1 and x == -1 and y == -1:
            back_d = (d + 2) % 4  # 반대 방향
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]
            nx = r + dx[back_d]
            ny = c + dy[back_d]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 1:
                r, c = nx, ny
            else:
                print(answer)
                break

        else:
            visited[x][y]=True
            answer+=1
            d=direction
            r,c=x,y


solution(r,c,d,visited)