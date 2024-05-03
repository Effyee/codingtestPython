def solution(p):
    return dfs(p)

def is_balanced(s):
    left,right=0,0
    for i in range(len(s)):
        if s[i]=='(':
            left+=1
        else:
            right+=1
        if left==right:
            return s[:i+1],s[i+1:]

def is_correct(s):
    stack=[]
    for i in range(len(s)):
        if s[i]=='(':
            stack.append('(')
        else:
            if len(stack)==0:
                return False
            else:
                stack.pop()
    if not stack:
        return True
    else:
        return False

def dfs(s):
    if s=='':
        return ''
    u,v=is_balanced(s)
    
    if is_correct(u):
        return u+dfs(v)
    
    else:
        s1='('+dfs(v)+')'
        s2=''
        s3=u[1:-1]
        for i in s3:
            if i=='(':
                s2+=')'
            else:
                s2+='('
        return s1+s2

