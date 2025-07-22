import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

n,m=map(int,input().split())
parent=[i for i in range(n+1)]

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union(a,b,parent):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for _ in range(m):
    check,a,b=map(int,input().split())
    # a==0 이면 a가 들어간 집합과 b가 들어있는 집합을 합치자
    if check==0:
        union(a,b,parent)
    else:
        if find_parent(parent,a)==find_parent(parent,b):
            print("yes")
        else:
            print("no")