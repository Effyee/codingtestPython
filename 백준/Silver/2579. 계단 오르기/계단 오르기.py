n=int(input())
value=[0]
for _ in range(n):
    value.append(int(input()))
dp=[0]*(n+1)

def solution(n,value):
    
    if n<=2:
        return(sum(value))
    else:
        dp[1]=value[1]
        dp[2]=value[1]+value[2]
        for i in range(3,n+1):
            dp[i]=max(dp[i-2]+value[i],dp[i-3]+value[i-1]+value[i])
        return dp[n]

print(solution(n,value))