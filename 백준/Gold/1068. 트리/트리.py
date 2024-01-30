import sys

n=int(sys.stdin.readline().rstrip())
tree=list(map(int,sys.stdin.readline().rsplit()))


def dfs(v,tree):
    tree[v]=-2
    for i in range(n):
        if v==tree[i]:
            dfs(i,tree)

v=int(sys.stdin.readline().rstrip())
dfs(v,tree)


answer = 0

for i in range(n):
    if tree[i] != -2 and i not in tree: #-2는 지우는 노드들 // i노드의 자식이 트리 안에 없으면 == 리프노드임
        answer+=1

print(answer)