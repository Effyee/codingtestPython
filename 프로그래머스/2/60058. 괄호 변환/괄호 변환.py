def solution(p):
    return dfs(p)


def divide(s):
    left,right=0,0
    for i in range(len(s)):
        if s[i]=='(':
            left+=1
        else:
            right+=1
        if left==right:
            return s[:i+1],s[i+1:]


def check(s):
    stack=[]
    for i in range(len(s)):
        if s[i]=='(':
            stack.append('(')
        else:
            if len(stack)==0:
                return False
            else:
                stack.pop()
    if len(stack)==0:
        return True
    
def dfs(p):   
    if p=='':
        return ''
    u,v=divide(p)
    if check(u):
        return u+dfs(v)
    else:
        s1='('+dfs(v)+')'
        u=u[1:-1]
        s2=''
        for i in range(len(u)):
            if u[i]=='(':
                s2+=')'
            else:
                s2+='('
    return s1+s2
        