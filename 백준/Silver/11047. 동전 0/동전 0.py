import sys
input=sys.stdin.readline

n,k=map(int,input().split())
coins=[int(input()) for _ in range(n)]
coins=sorted(coins,reverse=True)
answer=0
for coin in coins:
    if k>=coin:
        answer+=k//coin
        k=k%coin
print(answer)