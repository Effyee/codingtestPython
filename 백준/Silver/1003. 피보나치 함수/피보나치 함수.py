t=int(input())

def solution(n):
    dp0=[0]*100001
    dp0[0]=1
    dp0[1]=0
    dp0[2]=1
    dp0[3]=1
    dp1=[0]*100001
    dp1[1]=1
    dp1[2]=1
    dp1[3]=2

    for i in range(4,n+1):
        dp0[i]=dp0[i-1]+dp0[i-2]
        dp1[i]=dp1[i-1]+dp1[i-2]
    return dp0[n],dp1[n]

for i in range(t):
    n=int(input())
    a,b=solution(n)
    print(a,b)