import sys
input=sys.stdin.readline

n,m=map(int,input().split())
parent=[i for i in range(n+1)]
edges=[]

for _ in range(m):
    start,des,cost=map(int,input().split())
    edges.append((cost,start,des))

def find_parent(x,parent):
    if parent[x]!=x:
        parent[x]=find_parent(parent[x],parent)
    return parent[x]

def make_union(a,b,parent):
    a=find_parent(a,parent)
    b=find_parent(b,parent)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

edges.sort()
result=0
last=0
for edge in edges:
    cost,a,b=edge
    if find_parent(a,parent)!=find_parent(b,parent):
        make_union(a,b,parent)
        result+=cost
        last=cost
        
print(result-last)