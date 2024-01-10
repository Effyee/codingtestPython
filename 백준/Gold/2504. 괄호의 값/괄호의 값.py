def isitbracket(s):
    stack = []
    for char in s:
        if char in ['(', '[']:
            stack.append(char)
        else:
            if not stack:
                return False
            if char == ')' and stack[-1] != '(':
                return False
            if char == ']' and stack[-1] != '[':
                return False
            stack.pop()
    return len(stack) == 0

def calculate(s):
    stack = []
    for char in s:
        if char in ['(', '[']:
            stack.append(char)
        elif char == ')':
            if stack[-1] == '(':
                stack[-1] = 2
            else:
                temp = 0
                while stack[-1] != '(':
                    temp += stack.pop()
                stack[-1] = temp * 2
        elif char == ']':
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                temp = 0
                while stack[-1] != '[':
                    temp += stack.pop()
                stack[-1] = temp * 3
    return sum(stack)

import sys

def input():
    return sys.stdin.readline().rstrip()

s = input()

if isitbracket(s):
    print(calculate(s))  # 출력: 42
else:
    print(0) 