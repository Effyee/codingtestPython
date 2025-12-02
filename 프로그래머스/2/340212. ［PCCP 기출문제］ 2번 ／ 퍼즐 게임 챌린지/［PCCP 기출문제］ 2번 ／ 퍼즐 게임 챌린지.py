def solution(diffs, times, limit):
    def calculate(level):
        t=0
        for i in range(len(diffs)):
            if diffs[i]<=level:
                t+=times[i]
            else:
                retry=diffs[i]-level
                if i>=1:
                    t+=(times[i-1]+times[i])*retry+times[i]
                else:
                    t+=times[i]
            if t > limit:  
                return t
        return t
    
    answer = 0
    start,end=1,max(diffs)
    while start<=end:
        mid=(start+end)//2
        ans=calculate(mid)
        if ans<=limit:
            answer=mid
            end=mid-1
        else:
            start=mid+1
    
    return answer