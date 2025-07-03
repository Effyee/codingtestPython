import sys
input=sys.stdin.readline


t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    dist=y-x
    tmp=0 # 이동 거리
    cnt=0 # 공간 장치 이동 횟수
    moving=0 # 반복 횟수

    while tmp<dist:
        # 홀수 일 때 마다 반복횟수 증가
        cnt+=1
        if cnt%2!=0:
            moving+=1
        tmp+=moving
    print(cnt)
