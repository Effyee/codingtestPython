def solution(name, yearning, photo):
    answer=[]
    dic=dict(zip(name,yearning))
    for people in photo:
        score=0
        for p in people:
            score+=dic.get(p,0)
        answer.append(score)
    return answer