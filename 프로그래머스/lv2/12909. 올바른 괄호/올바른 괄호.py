def solution(s):
    a=list(s)
    b=[]
    for aa in a:
        if len(b)==0:
            b.append(aa)
        elif b[-1]=='(' and aa==')':
            b.pop()
        else:
            b.append(aa)
    if len(b)==0:
        return True
    else:
        return False
    
            
    