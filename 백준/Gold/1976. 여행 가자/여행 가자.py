import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

# 도시 개수:N
n=int(input())
# 여행 계획에 속한 도시의 수:M
M=int(input())
# 양방향 도로
graph=[list(map(int,input().split())) for _ in range(n)]
trip=list(map(int,input().split()))
trip=[trip[i]-1 for i in range(len(trip))]

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
    return

parent=[i for i in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            make_union(i,j,parent)

for i in range(M-1):
    if find_parent(trip[i], parent) != find_parent(trip[i+1], parent):
        print('NO')
        exit()
print('YES')
