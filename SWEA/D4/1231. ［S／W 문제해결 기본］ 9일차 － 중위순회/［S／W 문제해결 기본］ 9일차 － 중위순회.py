from collections import defaultdict

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(node):
    global ans
    if node.left:
        inorder(tree[node.left])
    ans += node.data
    if node.right:
        inorder(tree[node.right])

T = 10

for case in range(1, T + 1):
    ans = ""
    N = int(input())
    tree = defaultdict(Node)

    for _ in range(N):
        arr = list(input().split())
        tree[int(arr[0])] = Node(arr[1])
        if len(arr) > 2:
            tree[int(arr[0])].left = int(arr[2])
            if len(arr) > 3:
                tree[int(arr[0])].right = int(arr[3])

    inorder(tree[1])
    print(f"#{case} {ans}")
