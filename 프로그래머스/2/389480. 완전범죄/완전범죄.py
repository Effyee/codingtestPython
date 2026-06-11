def solution(info, n, m):
    answer = 0
    INF=int(1e9)
    dp=[INF]*m
    dp[0]=0
    for a_trace, b_trace in info:
        new_dp=[INF]*m
        for prev_b in range(m):
            if(dp[prev_b]==INF):
                continue
            new_a=dp[prev_b]+a_trace
            if(new_a<n):
                new_dp[prev_b]=min(new_a, new_dp[prev_b])
            new_b=prev_b+b_trace
            if(new_b<m):
                new_dp[new_b]=min(dp[prev_b],new_dp[new_b])
        dp=new_dp
    answer=min(dp)
    if(answer==INF):
        return -1
    return answer