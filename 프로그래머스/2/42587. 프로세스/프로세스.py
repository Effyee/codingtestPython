def solution(priorities, location):
    answer = 0
    i, cnt = 0, 0
    l = []
    for i, p in enumerate(priorities):
        l.append((p,i ))
    print(l)
    while l :
        i+=1
        priority = max(l)
        priority=priority[0]
        if priority == l[0][0] and location == l[0][1]:
            return cnt + 1
        elif priority == l[0][0]:
            cnt += 1
            l.pop(0)
        else:
            l.append(l.pop(0))

    return answer