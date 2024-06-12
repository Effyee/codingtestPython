def solution(n):
    answer = 0
    for i in range(1,n+1):
        s=0
        num=i
        while s<n:
            s+=num
            if s==n:
                answer+=1
                break
            num+=1


    return answer