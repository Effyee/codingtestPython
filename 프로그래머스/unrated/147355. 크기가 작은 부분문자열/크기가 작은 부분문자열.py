def solution(t, p):
    answer = 0
    length=len(p)
    s=0
    for i in range(len(t)):
        if len(t[i:i+length])>=length:
            if int(t[i:i+length])<=int(p):
                answer+=1
    return answer