N=int(input())
dp=list([0]*10 for _ in range(N+1))
dp[1]=[1]*10 # 첫 행은 모두 1
for i in range(2,N+1):# 2부터 N+1까지만
    for j in range(10):
        if j==0: #첫 열은 모두 1
            dp[i][j]=1
        else:
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
print(sum(dp[N])%10007)