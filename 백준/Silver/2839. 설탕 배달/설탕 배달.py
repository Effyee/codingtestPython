import sys
input=sys.stdin.readline

n=int(input())
dp=[0]*(5000+1)
dp[0]=0
dp[1]=-1
dp[2]=-1
dp[3]=1
dp[4]=-1
dp[5]=1
for i in range(6,n+1):
    if i%5==0:
        dp[i]=i//5
    elif (i-3)%3==0 or (i-3)%5==0 or dp[i-3]!=-1:
        dp[i]=dp[i-3]+1
    else:
        dp[i]=-1

print(dp[n])