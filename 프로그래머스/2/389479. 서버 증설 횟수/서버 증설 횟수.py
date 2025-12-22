def solution(players, m, k):
    answer = 0
    # 현재 서버 대수: n
    n=0
    s=[]
    for player in players:
        if n>0:
            for i in range(len(s)-1,-1,-1):
                s[i]-=1
                if s[i]==0:
                    s.pop(i)
                    n-=1
            
        if player>=(n+1)*m:
            needed_server=player//m
            added_server=needed_server-n
            n+=added_server
            answer+=added_server
            s+=[k]*added_server
        
        
    return answer