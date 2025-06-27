import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
    # 동전의 가지 수
    N=int(input())
    moneys=list(map(int,input().split()))
    # 목표 금액
    m=int(input())
    dp=[0]*(m+1)
    dp[0]=1
    for money in moneys:
        for i in range(money,m+1):
            dp[i]+=dp[i-money]
    print(dp[-1])