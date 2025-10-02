def solution(n, times):
    answer = 0
    times.sort()
    start,end=1,times[-1]*n
    while start<=end:
        mid=(start+end)//2
        count=0
        for time in times:
            count+=mid//time
        if count>=n:
            answer=mid
            end=mid-1
        else:
            start=mid+1
    return answer