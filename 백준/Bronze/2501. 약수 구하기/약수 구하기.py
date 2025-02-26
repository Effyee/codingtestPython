import sys
input=sys.stdin.readline

N,K=map(int,input().split())
answer=[]

for i in range(1,N+1):
    if N%i==0:
        answer.append(i)

if len(answer)>=K:
    print(answer[K-1])
else:
    print(0)