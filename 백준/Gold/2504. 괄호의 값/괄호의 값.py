import sys

def isitbraket(s):
    stack=[]
    for char in s:
        if char in ['[','(']:
            stack.append(char)
        else:
            if not stack:
                return False
            if char==')' and stack[-1]!='(':
                return False
            if char==']' and stack[-1]!='[':
                return False
            stack.pop()
    return len(stack)==0

def calculate(s):
    expression=[]
    answer=[]
    for char in s:
        if char in ['(','[']:
            expression.append(char)
        else:
            if char==')':
                if expression[-1]=='(':
                    expression.pop()
                    expression.append(2)
                else:
                    temp=0
                    while expression[-1]!='(':
                        temp+=expression[-1]
                        expression.pop()
                    expression.pop()
                    expression.append(2 * temp)
            if char==']':
                if expression[-1]=='[':
                    expression.pop()
                    expression.append(3)
                else:
                    temp=0
                    while expression[-1]!='[':
                        temp+=expression[-1]
                        expression.pop()
                    expression.pop()
                    expression.append(3 * temp)


    return sum(expression)


s=sys.stdin.readline().rstrip()

if isitbraket(s):
    print(calculate(s))
else:
    print(0)
