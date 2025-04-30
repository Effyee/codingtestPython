import sys
input=sys.stdin.readline

n,k=map(int,input().split())
coins=[]
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)
answer=0
idx=0
while k>0:
    while k>=coins[idx]:
        answer += (k // coins[idx])
        k=k-(k//coins[idx])*coins[idx]
    idx+=1
    if idx==len(coins):
        break

print(answer)