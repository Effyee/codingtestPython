from collections import defaultdict

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def postorder(node):
    global answer
    if node.left:
        postorder(tree[node.left])
    if node.right:
        postorder(tree[node.right])
    answer.append(node.data)

def calculate(l):
    stack=[]
    for i in range(len(l)):
        if l[i]=='+':
            b=stack.pop()
            a=stack.pop()
            stack.append(int(a)+int(b))

        elif l[i]=='-':
            b = stack.pop()
            a = stack.pop()
            stack.append(int(a)-int(b))

        elif l[i]=='*':
            b = stack.pop()
            a = stack.pop()
            stack.append(int(a)*int(b))

        elif l[i]=='/':
            b = stack.pop()
            a = stack.pop()
            stack.append(int(a)//int(b))

        else:
            stack.append(int(l[i]))

    return stack[-1]

for _ in range(10):
    n=int(input())
    tree=defaultdict(Node)
    answer=[]
    for i in range(n):
        arr=list(input().split())
        tree[int(arr[0])]=Node(arr[1])
        if len(arr)>2:
            tree[int(arr[0])].left=int(arr[2])
            if len(arr)>3:
                tree[int(arr[0])].right=int(arr[3])

    postorder(tree[1])
    print(f'#{_+1} {calculate(answer)}')