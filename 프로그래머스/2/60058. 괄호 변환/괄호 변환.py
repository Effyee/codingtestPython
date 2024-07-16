def solution(p):
    if check(p):
        return p
    else:
        return dfs(p)


def check(p):
    stack = []
    for i in range(len(p)):
        if not stack:
            stack.append(p[i])
        else:
            if p[i] == "(":
                stack.append(p[i])
            elif p[i] == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
    if not stack:
        return True
    return False

def divide(p):
    right, left = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return p[:i+1], p[i+1:]
    return None, None

def dfs(p):
    if p == '':
        return p
    else:
        u, v = divide(p)
        if u is None or v is None:
            return '(' + dfs(p) + ')'
        if check(u):
            return u + dfs(v)
        else:
            s1='(' + dfs(v) + ')'
            s2=u[1:-1]
            s3=''
            for i in range(len(s2)):
                if s2[i]=='(':
                    s3+=')'
                else:
                    s3+='('
            return s1+s3