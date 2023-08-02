def solution(s):
    a=list(s)
    b=[]
    for i in a:
        if len(b)==0:
            b.append(i)
        elif b[-1]=='(' and i==')':
            b.pop()
        else:
            b.append(i)
    if len(b)==0:
        return True
    else:
        return False
    
            
    