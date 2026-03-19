import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
candy=list(map(int,input().split()))
parent=[i for i in range(n+1)]

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

for _ in range(m):
    a,b=map(int,input().split())
    make_union(a,b,parent)

group_candy=[0]*(n+1)
group_size=[0]*(n+1)

for i in range(1, n+1):
    root = find_parent(i,parent)
    group_size[root] += 1
    group_candy[root] += candy[i-1]

groups = []
for i in range(1, n+1):
    if group_size[i] > 0:
        groups.append((group_size[i], group_candy[i]))

dp = [[0]*k for _ in range(len(groups)+1)]

for i in range(1, len(groups)+1):
    size, candy = groups[i-1]
    for j in range(k):
        if j >= size:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-size] + candy)
        else:
            dp[i][j] = dp[i-1][j]
print(max(dp[len(groups)]))

