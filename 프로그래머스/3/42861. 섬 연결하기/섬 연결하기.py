import sys
input=sys.stdin.readline
sys.setrecursionlimit(int(1e6))
def solution(n, costs):
    answer = 0
    costs=sorted(costs,key= lambda x:x[2])
    parent=[i for i in range(n)]
    def find_parent(x,parent):
        if parent[x]!=x:
            parent[x]=find_parent(parent[x],parent)
        return parent[x]
    
    def make_union(a,b,parent):
        a=find_parent(a,parent)
        b=find_parent(b,parent)
        if a<=b:
            parent[b]=a
        else:
            parent[a]=b
    
    for start,end,cost in costs:
        if find_parent(start,parent)!=find_parent(end,parent):
            answer+=cost
            make_union(start,end,parent)
        
            
    return answer