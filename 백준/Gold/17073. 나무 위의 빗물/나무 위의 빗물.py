import sys

n,w=map(int,sys.stdin.readline().rsplit())

tree=[[] for i in range(n+1)]

for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().rsplit())
    tree[a].append(b)
    tree[b].append(a)


leaf=0
for i in range(2,len(tree)):
    if len(tree[i])==1:
        leaf+=1

print(w/leaf)
