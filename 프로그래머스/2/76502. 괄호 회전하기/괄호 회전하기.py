from collections import deque

def isitbracket(q):
    q1 = []
    for char in q:
        if char in '([{':
            q1.append(char)
        elif char in ')]}':
            if len(q1) == 0:
                return False
            if char == ')' and q1[-1] == '(':
                q1.pop()
            elif char == ']' and q1[-1] == '[':
                q1.pop()
            elif char == '}' and q1[-1] == '{':
                q1.pop()
    
    return len(q1) == 0

def solution(s):
    answer = 0
    s = deque(s)
    
    for _ in range(len(s)):
        if isitbracket(s):
            answer += 1
        s.rotate(1)
    
    return answer
