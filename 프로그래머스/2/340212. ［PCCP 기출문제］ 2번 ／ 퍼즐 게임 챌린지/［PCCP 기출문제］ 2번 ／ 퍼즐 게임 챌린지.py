def solution(diffs, times, limit):
    answer = 0
    
    def spending_time(level):
        time=0
        time_prev=0
        for i in range(len(diffs)):
            if level>=diffs[i]:
                time+=times[i]
            else:
                d=diffs[i]-level
                time+=(time_prev+times[i])*d+times[i]
            time_prev=times[i]
        return time
    
    start,end=1, max(diffs)
    while start<=end:
        mid=(start+end)//2
        time=spending_time(mid)
        if time<=limit:
            answer=mid
            end=mid-1
        else:
            start=mid+1
        
    return answer