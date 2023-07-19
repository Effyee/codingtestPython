def solution(name, yearning, photo):
    result = []
    dic = dict(zip(name, yearning))
    for people in photo:
        score = 0
        for person in people:
            score += dic.get(person, 0)
        result.append(score)
    
    return result
  