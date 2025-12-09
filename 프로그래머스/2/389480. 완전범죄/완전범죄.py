def solution(info, n, m):
    answer = 0
    INF=int(1e9)
    dp=[INF]*m
    dp[0]=0
    for a_trace,b_trace in info:
        new_dp=[INF]*(m)
        for prev_b in range(m):
            if dp[prev_b]==INF:
                continue
            # A가 훔치는 경우
            a_new=a_trace+dp[prev_b]
            if a_new<n:
                new_dp[prev_b]=min(a_new,new_dp[prev_b])
            # B가 훔치는 경우
            b_new=b_trace+prev_b
            if b_new<m:
                new_dp[b_new]=min(dp[prev_b],new_dp[b_new])
        dp=new_dp
    if min(dp)==INF:
        return -1
    return min(dp)