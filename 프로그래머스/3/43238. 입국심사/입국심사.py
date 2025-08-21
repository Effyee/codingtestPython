def solution(n, times):
    answer = 0
    # n: 기다리는 사람 수, times: 한 명을 심사하는 데 걸리는 시간
    times.sort()
    start,end=times[0],times[-1]*n
    
    while start<=end:
        mid=(start+end)//2
        print(f"start:{start}, end:{end}, mid:{mid}")
        re=0
        for time in times:
            re+=mid//time
        print(re)
        if re>=n:
            answer=mid
            end=mid-1
        else:
            start=mid+1
            
    return answer