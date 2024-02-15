import sys


t=int(sys.stdin.readline().rstrip())

def solution():
    n = int(sys.stdin.readline().rstrip())
    tree=[0 for _ in range(n+1)]

    for _ in range(n-1):
        a,b=map(int,sys.stdin.readline().rsplit())
        tree[b]=a

    c1,c2=map(int,sys.stdin.readline().rsplit())

    p1=[c1]
    while tree[c1] != 0:
        c1 = tree[c1]
        p1.append(c1)

    p2=[c2]
    while tree[c2] != 0:
        c2 = tree[c2]
        p2.append(c2)

    for i in p1:
        if i in p2:
            print(i)
            break

for _ in range(t):
    solution()