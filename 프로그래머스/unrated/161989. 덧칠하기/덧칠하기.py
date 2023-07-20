def solution(n, m, section):
    answer=0
    paint = [0]*(2*int(n))
    for s in section:
        paint[s]=1
    for i in range(len(paint)):
        if paint[i]==1:
            for j in range(m):
                paint[i+j]-=1
            answer+=1
            
    return answer