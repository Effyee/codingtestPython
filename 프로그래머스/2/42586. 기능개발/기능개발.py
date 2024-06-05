import math

def solution(progresses, speeds):
    answer = []
    days=[math.ceil((100-p)/s) for (p,s) in zip(progresses,speeds)]
    max_days=days[0]
    cnt=1
    for i in range(1,len(days)):
        if days[i]<=max_days:
            cnt+=1
        else:
            max_days=days[i]
            answer.append(cnt)
            cnt=1
    answer.append(cnt)

    return answer