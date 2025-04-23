import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))

li=[arr[0]]

def binary_search(li,x):
    start,end=0,len(li)-1
    while start<=end:
        mid=(start+end)//2
        if li[mid]<x:
            start=mid+1
        else:
            end=mid-1
    return start

for i in range(1,n):
    if li[-1]<arr[i]:
        li.append(arr[i])
    else:
        idx=binary_search(li,arr[i])
        li[idx]=arr[i]

print(len(li))