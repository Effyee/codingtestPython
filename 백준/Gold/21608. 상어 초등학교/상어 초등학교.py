import sys
input=sys.stdin.readline

#조건1) 좋아하는 학생인 인접한 칸에 많은
#조건2) 1이 여러개, 인접 칸중 빈칸 많은
#조건3) 2가 여러개, 행의 번호가 가장 작은칸

N=int(input())
students=[[] for _ in range((N*N)+1)]

graph=[[0]*(N) for _ in range(N)]

def like_count(student,x,y):
    cnt=0
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if graph[nx][ny] in students[student]:
                cnt+=1
    return cnt,x,y

def vacant_count(x,y):
    vcnt=0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny]==0:
                vcnt += 1
    return vcnt

def solution(a):
    lcnt = 0
    cnd = []
    for i in range(N):
        for j in range(N):
            if graph[i][j]==0:
                cnt,x,y=like_count(a,i,j)
                if cnt>lcnt:
                    lcnt=cnt
                    cnd=[[x,y]]
                elif cnt==lcnt:
                    cnd.append([x,y])
    if len(cnd)==1:
        x,y=cnd[0][0],cnd[0][1]
        graph[x][y]=a
    else:
        svcnt = -1
        vcnd = []
        for x,y in cnd:
            vcnt=vacant_count(x,y)
            if svcnt<vcnt:
                svcnt=vcnt
                vcnd=[[x,y]]
            elif svcnt==vcnt:
                vcnd.append([x,y])

        if len(vcnd)==1:
            x, y = vcnd[0][0], vcnd[0][1]
            graph[x][y] = a
        else:
            vcnd=sorted(vcnd,key=lambda x:(x[0],x[1]))
            graph[vcnd[0][0]][vcnd[0][1]]=a
for _ in range((N*N)):
    a,b,c,d,e=map(int,input().split())
    students[a].append(b)
    students[a].append(c)
    students[a].append(d)
    students[a].append(e)
    solution(a)

answer=0
for i in range(N):
    for j in range(N):
        cnt,x,y=like_count(graph[i][j],i,j)
        if cnt==4:
            answer+=1000
        elif cnt==3:
            answer+=100
        elif cnt==2:
            answer+=10
        elif cnt==1:
            answer+=1

print(answer)