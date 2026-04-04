import sys
input=sys.stdin.readline

n,m=map(int,input().split())
def bt(li):
    if len(li)==m:
        print(*li)
        return
    for i in range(1,n+1):
        bt(li+[i])
    return

bt([])