import sys
input=sys.stdin.readline

n,m=map(int,input().split())
answer=[]

def backtrack(i):
    global answer
    if len(answer)==m:
        print(' '.join(map(str,answer)))
        return
    for j in range(i,n+1):
        answer.append(j)
        backtrack(j)
        answer.pop()
    return

backtrack(1)