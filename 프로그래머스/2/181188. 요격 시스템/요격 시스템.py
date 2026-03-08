def solution(targets):
    answer = 1
    targets.sort()
    start,end=targets[0]
    for i in range(1,len(targets)):
        nstart,nend=targets[i]
        if end<=nstart:
            answer+=1
            start,end=nstart,nend
        else:
            start=nstart
            if nend<=end:
                end=nend
    return answer