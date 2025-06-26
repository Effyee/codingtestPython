import sys
input=sys.stdin.readline

n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)]
dp[0][0]=1

for x in range(n):
    for y in range(n):
        if x==n-1 and y==n-1:
            continue
        dist=graph[x][y]
        if x+dist<n:
            dp[x+dist][y]+=dp[x][y]
        if y+dist<n:
            dp[x][y+dist]+=dp[x][y]

print(dp[-1][-1])