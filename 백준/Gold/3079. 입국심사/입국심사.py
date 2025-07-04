import sys
input=sys.stdin.readline

# 입국 심사대 n개,m명
n,m=map(int,input().split())
t=[int(input()) for _ in range(n)]
t.sort()
start,end=1,t[-1]*m
answer=0

while start<=end:
    mid=(start+end)//2
    total=0
    for time in t:
        total+=(mid//time)
    # 더 작은 시간도 가능한지 확인
    if total>=m:
        answer=mid
        end=mid-1
    else:
        start=mid+1

print(answer)
