import sys

def solution(s):
    stack=[]
    answer=''
    for char in s:
        if char.isalpha():
            answer+=char
        else:
            if char=='(':
                stack.append(char)
            if char in ['*','/']:
                while stack and stack[-1] in ['*','/']:
                    answer+=stack.pop()
                stack.append(char)
            if char in ['+','-']:
                while stack and stack[-1] in ['*','/','+','-']:
                    answer+=stack.pop()
                stack.append(char)
            if char==')':
                while stack and stack[-1] != '(':
                    answer+=stack.pop()
                stack.pop()
    while stack:
        answer+=stack.pop()
    print(answer)

s=sys.stdin.readline().rstrip()

solution(s)
