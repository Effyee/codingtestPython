import sys
input=sys.stdin.readline

n,m=map(int,input().split())
l=[0]+[int(input()) for _ in range(n)]
INF=int(1e9)
tree=[0]*(4*n)
def segment(left,right,idx=1):
    if left==right:
        tree[idx]=l[left]
        return tree[idx]
    mid=(left+right)//2
    tree[idx]=min(segment(left,mid,idx*2),segment(mid+1,right,idx*2+1))
    return tree[idx]

def search(start,end,left,right,i=1):
    # start,end: 현재 구간
    # left, right: 찾고자하는 구간
    if end<left or start>right:
        return INF
    elif start>=left and end<=right:
        return tree[i]
    else:
        mid=(start+end)//2
        return min(search(start,mid,left,right,i*2),search(mid+1,end,left,right,i*2+1))


segment(1,n)


for _ in range(m):
    a,b=map(int,input().split())
    print(search(1, n,a,b))
