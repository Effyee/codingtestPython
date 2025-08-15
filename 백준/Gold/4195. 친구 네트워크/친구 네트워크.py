import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def find_parent(x,parent):
    if parent[x]!=x:
        parent[x]=find_parent(parent[x],parent)
    return parent[x]

def make_union(a,b,parent):
    a=find_parent(a,parent)
    b=find_parent(b,parent)
    if a==b:
        return network[a]
    if a<b:
        parent[b]=a
        network[a]+=network[b]
        return network[a]
    else:
        parent[a]=b
        network[b]+=network[a]
        return network[b]

t=int(input())
for _ in range(t):
    f=int(input())
    parent={}
    network={}
    for _ in range(f):
        A,B=list(map(str,input().split()))
        if A not in parent:
            parent[A]=A
            network[A]=1
        if B not in parent:
            parent[B]=B
            network[B]=1

        result=make_union(A,B,parent)
        print(result)
