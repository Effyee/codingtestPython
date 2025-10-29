import sys
input=sys.stdin.readline

n=int(input())

lines=[list(map(int,input().split())) for _ in range(n)]
lines=sorted(lines,key=lambda x:(x[0],x[1]))

start,end=lines[0][0],lines[0][1]
answer=0
for i in range(1,n):
    if start<=lines[i][0]<=end:
        end=max(end,lines[i][1])
    else:
        answer+=end-start
        start,end=lines[i]
print(answer+end-start)
