def solution(s):
    stack=[]
    for i in range(len(s)):
        if not stack:
            if s[i]=='(':
                stack.append(s[i])
            else:
                return False
        else:
            if s[i]==')':
                if stack[-1]!='(':
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])
    if not stack:
        return True
    return False