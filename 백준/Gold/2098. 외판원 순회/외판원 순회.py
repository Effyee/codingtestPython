import sys
input=sys.stdin.readline
INF=int(1e9)

n=int(input())
mat=[list(map(int,input().split())) for _ in range(n)]
# dp[직전에 방문했던 도시][지금까지 방문한 도시 체크(비트마스크)]
dp=[[None]*(1<<n) for _ in range(n)]

# node: 현재 도시, chk: 지금까지 방문한 도시 체크
def dfs(node,chk):
    # 모든 도시를 다돌았을 때
    if chk==(1<<n)-1:
        # 출발 도시로 돌아갈 수 있다면
        if mat[node][0]!=0:
            return mat[node][0]
        else:
            return INF
    # 이미 방문했던 경로, 도시라면
    if dp[node][chk]:
        return dp[node][chk]
    min_value=INF
    # 모든 도시들을 돌면서
    for i in range(1,n):
        # 갈 수 있는 경로이고 ,이 경로가 방문한 적이 없다면
        if mat[node][i]!=0 and (chk&(1<<i))==0:
            min_value=min(min_value,dfs(i,(chk|1<<i))+mat[node][i])
    dp[node][chk]=min_value
    return min_value

# 0 번 도시 부터 시작
# 어떤 도시부터 방문해도 상관없음 어짜피 cycle이기 때문에
answer=dfs(0,1)
print(answer)