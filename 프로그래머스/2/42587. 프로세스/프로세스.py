def solution(priorities, location):
    answer = 0
    while priorities:
        print(priorities,location,answer)
        priority=max(priorities)
        now=priorities.pop(0)
        if now!=priority:
            priorities.append(now)
            if location-1<0:
                location=len(priorities)-1
            else:
                location-=1
        else:
            if location==0:
                return answer+1
            else:
                answer+=1
                location-=1
    return answer