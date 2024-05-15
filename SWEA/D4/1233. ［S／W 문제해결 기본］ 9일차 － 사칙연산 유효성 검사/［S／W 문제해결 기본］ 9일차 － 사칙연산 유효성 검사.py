from collections import defaultdict

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(node):
    global answer
    if node.left:
        inorder(tree[node.left])
    answer+=node.data
    if node.right:
        inorder(tree[node.right])

for _ in range(10):
    n=int(input())
    tree=defaultdict(Node)
    answer=''
    for i in range(n):
        arr=list(input().split())
        tree[int(arr[0])]=Node(arr[1])
        if len(arr)>2:
            tree[int(arr[0])].left=int(arr[2])
            if len(arr)>3:
                tree[int(arr[0])].right=int(arr[3])

    inorder(tree[1])
    nums=['0','1','2','3','4','5','6','7','8','9']


    result=1
    for i in range(len(list(answer))):
        if i%2==0:
            if answer[i] not in nums:
                result=0
                break
    print(f'#{_ + 1} {result}')