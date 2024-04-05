def divide(s):
    left,right=0,0
    for i in range(len(s)):
        if s[i]=='(':
            left+=1
        else:
            right+=1
        if left==right:
            return s[:i+1], s[i+1:]

def check(s):
    stack=[]
    for i in range(len(s)):
        if s[i]=='(':
            stack.append('(')
        else:
            if len(stack)==0:
                return False
            elif stack[-1]=='(':
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True
    return False

def dfs(s):
    if s == '':
        return ''
    u, v = divide(s)
    if check(u):
        return u + dfs(v)
    else:
        s_1 = '(' + dfs(v) + ')'
        s_2 = ''
        for char in u[1:-1]:  # u의 첫 번째와 마지막 문자를 제외하고 반복
            if char == '(':
                s_2 += ')'  # '('를 ')'로 변경
            else:
                s_2 += '('  # ')'를 '('로 변경
        return s_1 + s_2  # 수정된 부분: s_2와 s_1의 순서 변경

def solution(p):
    answer = ''
    answer=dfs(p)
    return answer


