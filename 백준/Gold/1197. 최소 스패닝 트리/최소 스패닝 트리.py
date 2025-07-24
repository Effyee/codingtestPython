import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
v,e=map(int,input().split())
parent=[i for i in range(v+1)]
edges=[]

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

# 각 간선 정보
for _ in range(e):
    start,end,cost=map(int,input().split())
    edges.append((cost,start,end))


edges.sort()
answer=0
for edge in edges:
    cost,start,end=edge
    if find_parent(start,parent)!=find_parent(end,parent):
        make_union(start, end, parent)
        answer+=cost


print(answer)

