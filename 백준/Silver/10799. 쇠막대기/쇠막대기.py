import sys
def solution(s):
    stack=[]
    answer=0
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(s[i])
        else:
            stack.pop()
            if s[i-1]=='(':
                answer+=len(stack)
            else:
                answer+=1
    print(answer)
s=sys.stdin.readline().rstrip()
solution(s)