import sys
input=sys.stdin.readline

n,m=map(int,input().split())

def backtrack(l,i):
    if i-1>n:
        return
    if len(l)==m:
        print(' '.join(map(str,l)))
        return
    l.append(i)
    backtrack(l,i+1)
    l.pop()
    backtrack(l,i+1)
    return

backtrack([],1)