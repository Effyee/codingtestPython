import sys
input=sys.stdin.readline

# 기차수, 명령수
n,m=map(int,input().split())
trains=[[0]*(21) for _ in range(n+1)]
for _ in range(m):
    # 명령 번호, i 번째 기차, x 번 좌석
    a=input().split()
    if len(a)==3:
        number=int(a[0])
        i=int(a[1])
        x=int(a[2])
    else:
        number=int(a[0])
        i=int(a[1])

    if number==1:
        if trains[i][x]==0:
            trains[i][x]=1
    elif number==2:
        if trains[i][x]==1:
            trains[i][x]=0
    elif number == 3:
        # 20번째 좌석은 무조건 하차
        trains[i][20] = 0
        # 19번째 좌석부터 1번째 좌석까지 한 칸씩 뒤로
        for b in range(19, 0, -1):  # 19부터 1까지 역순
            trains[i][b + 1] = trains[i][b]
        # 1번째 좌석은 비어있게 됨
        trains[i][1] = 0
    else:  # number == 4
        # 1번째 좌석은 무조건 하차
        trains[i][1] = 0
        # 2번째 좌석부터 20번째 좌석까지 한 칸씩 앞으로
        for b in range(1, 20):  # 1부터 19까지 순차
            trains[i][b] = trains[i][b + 1]
        # 20번째 좌석은 비어있게 됨
        trains[i][20] = 0

visited=[]
answer=0
for c in range(1,n+1):
    if trains[c] not in visited:
        visited.append(trains[c])
        answer+=1
    else:
        continue

print(answer)