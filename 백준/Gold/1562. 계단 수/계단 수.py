import sys
input=sys.stdin.readline
MOD=int(1e9)
N=int(input())
# dp[숫자 자리수][마지막 수][비트마스킹 방문여부체크(0~9)]
dp=[[[0]*1024 for _ in range(10)] for _ in range(N+1)]

# 초기화
for i in range(1,10):
    dp[1][i][1<<i]=1

# 자릿수
for n in range(2,N+1):
    for i in range(0,10):
        for bit in range(1024):
            # 마지막 수가 0인 경우 다음 오는 수는 1
            if i==0:
                dp[n][i][bit|(1<<i)]+=dp[n-1][i+1][bit]
            # 마지막 수가 9인 경우 다음 오는 수는 8
            elif i==9:
                dp[n][i][bit|(1<<i)]+=dp[n-1][i-1][bit]
            else:
                dp[n][i][bit|(1<<i)]+=(dp[n-1][i-1][bit]+dp[n-1][i+1][bit])
            dp[n][i][bit|(1<<i)]%=MOD

res=0
for i in range(10):
    res+=dp[N][i][2**10-1]

print(int(res%MOD))