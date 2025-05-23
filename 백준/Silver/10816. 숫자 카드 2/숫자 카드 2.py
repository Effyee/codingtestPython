import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
m=int(input())
targets=list(map(int,input().split()))

def lower_bound(target):
    start,end=0,len(arr)
    while start<end:
        mid=(start+end)//2
        if arr[mid]<target:
            start=mid+1
        else:
            end=mid
    return start

def upper_bound(target):
    start,end=0,len(arr)
    while start<end:
        mid=(start+end)//2
        if arr[mid]<=target:
            start=mid+1
        else:
            end=mid
    return start
answer=[]
for i in range(m):
    answer+=[upper_bound(targets[i])-lower_bound(targets[i])]

print(*answer)