import sys

def isitbracket(s):
    stack=[]
    for char in s:
        if char in ['(','[']:
            stack.append(char)
        else:
            if not stack:
                return False
            if stack[-1]=='(' and char!=')':
                return False
            if stack[-1]=='[' and char!=']':
                return False
            stack.pop()
    if len(stack)!=0:
        return False
    else:
        return True

def solution(s):
    stack=[]
    for char in s:
        if char in ['(','[']:
            stack.append(char)
        else:
            if char==')':
                if stack[-1]=='(':
                    stack.pop()
                    stack.append(2)
                else:
                    temp=0
                    while stack[-1]!='(':
                        temp+=stack.pop()
                    stack.pop()
                    stack.append(2*temp)
            else:
                if stack[-1]=='[':
                    stack.pop()
                    stack.append(3)
                else:
                    temp=0
                    while stack[-1]!='[':
                        temp+=stack.pop()
                    stack.pop()
                    stack.append(3*temp)
    print(sum(stack))



s=sys.stdin.readline().rstrip()

if isitbracket(s):
    solution(s)
else:
    print(0)