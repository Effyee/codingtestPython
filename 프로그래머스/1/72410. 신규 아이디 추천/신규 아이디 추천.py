def solution(new_id):
    answer = ''
    index=0
    valid=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-','_','.','0','1','2','3','4','5','6','7','8','9']
    ll=list(map(str,new_id))
    
    for l in range(len(ll)):
        if len(answer)==0 and ll[l]=='.':
            continue
        elif ll[l]=='.' and answer[-1]=='.':
            continue            
        elif ll[l].isupper():
            answer+=ll[l].lower()
            continue
        elif str(new_id[l]) not in valid:
            continue
        
        answer+=str(new_id[l])

    if len(answer) > 0 and answer[-1]=='.':
        answer=answer[:-1]
    
    if len(answer)==0: 
        answer+='a'*3
        
    if len(answer)>=16:
        answer=answer[:15]
        if len(answer) > 0 and answer[-1]=='.':
            answer=answer[:-1]
    if len(answer)<=2:
        while len(answer) < 3:
            answer += answer[-1]
            
    return answer

