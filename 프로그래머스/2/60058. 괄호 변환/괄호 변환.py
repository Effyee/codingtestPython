def solution(p):
    return bfs(p)


def is_balanced(s):
    left, right = 0, 0
    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return s[:i+1], s[i+1:]


def is_correct(s):
    q=[]
    for i in range(len(s)):
        if s[i]=='(':
            q.append(s[i])
        else:
            if not q:
                return False
            else:
                q.pop()
    if not q:
        return True

def bfs(s):
    if s=='':
        return ''

    u,v=is_balanced(s)
    if is_correct(u):
        return u+bfs(v)
    else:
        s1='('+bfs(v)+')'
        s2=u[1:-1]
        s3=''
        for i in range(len(s2)):
            if s2[i]=='(':
                s3+=')'
            else:
                s3+='('
        return s1+s3