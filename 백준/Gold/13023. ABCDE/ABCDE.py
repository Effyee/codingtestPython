import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bt(now,depth):
    if depth==4:
        print(1)
        exit()
    for nxt in graph[now]:
        if not visited[nxt]:
            visited[nxt] = True
            bt(nxt,depth+1)
            visited[nxt]=False
    return False

for i in range(n):
    visited=[False]*(n)
    visited[i]=True
    bt(i,0)

print(0)
