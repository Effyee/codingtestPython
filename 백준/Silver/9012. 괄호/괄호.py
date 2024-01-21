import sys

def solution(s):
    stack=[]
    for char in s:
        if char=='(':
            stack.append(char)
        else:
            if not stack:
                return 'NO'
            if stack[-1]!='(':
                return 'NO'
            stack.pop()
    if len(stack)==0:
        return 'YES'
    else:
        return 'NO'

n=int(sys.stdin.readline().rstrip())
for _ in range(n):
    s=sys.stdin.readline().rstrip()
    print(solution(s))