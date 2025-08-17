import sys
from collections import deque
input=sys.stdin.readline

n,m,k=map(int,input().split())
fertilizer=[list(map(int,input().split())) for _ in range(n)]
tree=[[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,age=map(int,input().split())
    tree[x-1][y-1].append(age)
graph=[[5]*n for _ in range(n)]

dx=[0,0,-1,1,-1,-1,1,1]
dy=[-1,1,0,0,-1,1,-1,1]

for _ in range(k):
    # 봄, 여름
    for x in range(n):
        for y in range(n):
            dead_tree = 0
            grown_tree = deque()
            for t in tree[x][y]:
                # 남아있는 비료의 양이 더 많다면
                if t<=graph[x][y]:
                    grown_tree.append(t+1)
                    graph[x][y]-=t
                else:
                    dead_tree+=t//2
            tree[x][y]=grown_tree
            graph[x][y]+=dead_tree

    # 가을, 겨울
    for x in range(n):
        for y in range(n):
            for t in tree[x][y]:
                if t%5==0:
                    for d in range(8):
                        nx=x+dx[d]
                        ny=y+dy[d]
                        if 0<=nx<n and 0<=ny<n:
                            tree[nx][ny].appendleft(1)
            graph[x][y]+=fertilizer[x][y]

answer=0
for i in range(n):
    for j in range(n):
        if len(tree[i][j])>0:
            answer+=len(tree[i][j])
print(answer)
