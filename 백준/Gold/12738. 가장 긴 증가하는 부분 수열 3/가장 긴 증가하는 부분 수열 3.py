import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))

def bs(target,li):
    start,end=0,len(li)-1
    while start<=end:
        mid=(start+end)//2
        # lower bound
        if li[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return start

li=[arr[0]]
for i in range(1,n):
    target=arr[i]
    if target>li[-1]:
        li.append(target)
    else:
        idx=bs(target,li)
        li[idx]=target

print(len(li))