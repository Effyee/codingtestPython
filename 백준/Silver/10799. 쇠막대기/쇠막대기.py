import sys

def solution(s):
    stack=[]
    result = 0
    for i in range(len(s)):
        if s[i]=='(':
            stack.append('(')
        else:
            if s[i-1] == '(':
                stack.pop()
                result += len(stack)
            else:
                stack.pop()
                result += 1
    return result

s = sys.stdin.readline().rstrip()
print(solution(s))
