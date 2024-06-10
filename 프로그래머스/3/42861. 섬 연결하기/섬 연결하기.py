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

    return parent

def solution(n, costs):
    answer = 0
    costs=sorted(costs,key=lambda x:x[2])
    parent=[i for i in range(n)]
    for cost in costs:
        a,b,c=cost
        if find_parent(a,parent)!=find_parent(b,parent):
            make_union(a,b,parent)
            answer+=c

    return answer