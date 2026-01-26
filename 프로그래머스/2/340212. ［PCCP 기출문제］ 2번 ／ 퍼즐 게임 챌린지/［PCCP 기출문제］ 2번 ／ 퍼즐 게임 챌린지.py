# 이분 탐색
def solution(diffs, times, limit):
    answer = 0
    def count_time(level):
        time,time_prev=0,0
        for i in range(len(diffs)):
            if diffs[i]<=level:
                time+=times[i]
                time_prev=times[i]
            elif diffs[i]>level:
                t=diffs[i]-level
                time+=(times[i]+time_prev)*t
                time+=times[i]
                time_prev=times[i]
        return time
    
    start,end=1,max(diffs)
    while start<=end:
        mid=(start+end)//2
        t=count_time(mid)
        if t<=limit:
            answer=mid
            end=mid-1
        else:
            start=mid+1
    return answer