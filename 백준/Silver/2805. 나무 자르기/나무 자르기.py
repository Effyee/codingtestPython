import sys
input=sys.stdin.readline

n,m=map(int,input().split())
trees=list(map(int,input().split()))
trees.sort()

def bs():
    answer=0
    start,end=0,max(trees)
    while start<=end:
        mid=(start+end)//2
        cnt=0
        for i in range(n):
            if trees[i]>mid:
                cnt+=trees[i]-mid
        if cnt>=m:
            answer=mid
            start=mid+1
        else:
            end=mid-1
    return answer

print(bs())