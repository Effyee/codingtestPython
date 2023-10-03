def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0,len(score),m):
        l=score[i:i+m]
        if len(l)<m:
            continue
        answer+=l[-1]*m
    return answer