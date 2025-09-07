import sys
input=sys.stdin.readline

n,m=map(int,input().split())

def bt(li,idx):
    if len(li)==m:
        print(*li)
        return
    for i in range(idx,n+1):
        li.append(i)
        bt(li,i+1)
        li.pop()
    return

bt([],1)
