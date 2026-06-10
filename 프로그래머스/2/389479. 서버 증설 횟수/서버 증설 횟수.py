from collections import deque
def solution(players, m, k):
    answer = 0
    q=deque()
    active=0
        
    for player in players:
        
        while q and q[0][0]==0:
            _,cnt=q.popleft()
            active-=cnt
        
        for i in range(len(q)):
            remain,cnt=q.popleft()
            q.append((remain-1,cnt))
            
        need=player//m
        
        if need>active:
            add=need-active
            active+=add
            answer+=add
            
            q.append((k-1,add))
    return answer