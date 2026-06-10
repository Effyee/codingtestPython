def solution(info, n, m):
    answer = 0
    INF=int(1e9)
    dp=[INF]*(m)
    dp[0]=0
    for a_trace,b_trace in info:
        new_dp=[INF]*(m)
        for prev_b in range(m):
            if dp[prev_b]==INF:
                continue
            #A가 훔침
            a_new=dp[prev_b]+a_trace
            if a_new<n:
                new_dp[prev_b]=min(a_new, new_dp[prev_b])
            #B가 훔침
            b_new=prev_b+b_trace
            if b_new<m:
                new_dp[b_new]=min(new_dp[b_new], dp[prev_b])
        dp=new_dp
    if min(dp)==INF:
        return -1
    return min(dp)