import sys
input = sys.stdin.readline

n = int(input())
people = [0]+list(map(int, input().split()))
dp = [0]*(n+1)
ans=0

for i in range(1,n+1) :
    dp[people[i]]=dp[people[i]-1]+1 # dp에는 내 전 사람의 lis 길이에 +1을 하여 기록해준다.
    ans=max(ans,dp[people[i]]) # 정답은 바로바로 갱신해준다.

print(n-ans)