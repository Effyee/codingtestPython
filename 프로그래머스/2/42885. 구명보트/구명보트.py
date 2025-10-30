# 최대 두명, 무게 제한
from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    q=deque(people)
    print(q)
    while q:
        if len(q)>1:
            re=q[0]+q[-1]
            if re<=limit:
                q.popleft()
                q.pop()
                answer+=1
                continue
        q.pop()
        answer+=1
        
    return answer