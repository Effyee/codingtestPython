import sys

n=int(sys.stdin.readline().rstrip())
tree=[[] for i in range(n+1)]

for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().rsplit())
    tree[a].append(b)
    tree[b].append(a)

q=int(sys.stdin.readline().rstrip())

for _ in range(q):
    t,k=map(int,sys.stdin.readline().rsplit())
    if t==1:
        if len(tree[k])<=1:
            print('no')
        else:
            print('yes')
    else:
        print('yes')
