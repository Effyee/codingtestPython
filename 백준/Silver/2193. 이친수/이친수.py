import sys
input=sys.stdin.readline

# 0으로 시작하지 않음
# 1이 연속으로 나타나지 않음

n=int(input())
dp=[0]*91
dp[1]=1
dp[2]=1
for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])