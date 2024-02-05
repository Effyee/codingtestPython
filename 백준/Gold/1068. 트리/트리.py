import sys

n=int(sys.stdin.readline().rstrip())
tree=list(map(int,sys.stdin.readline().rsplit()))

node=int(sys.stdin.readline().rstrip())

def dfs(node,tree):
    tree[node]=-2
    for i in range(len(tree)):
        if node==tree[i]:
            tree[i]=-2
            dfs(i,tree)


dfs(node,tree)
answer=0
for i in range(len(tree)):
    if tree[i]!=-2 and i not in tree:
        answer+=1

print(answer)