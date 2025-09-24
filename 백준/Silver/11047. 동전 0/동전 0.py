import sys
input=sys.stdin.readline

n,k=map(int,input().split())
coins=[int(input()) for i in range(n)]
coins=sorted(coins,reverse=True)
answer=0
for i in range(len(coins)):
    if k>=coins[i]:
        answer+=k//coins[i]
        k=k%coins[i]
print(answer)