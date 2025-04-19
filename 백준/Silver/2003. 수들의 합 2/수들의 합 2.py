import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))

start,end=0,0
total=0
count=0
while end<=n:
    if total<m:
        if end<n:
            total+=arr[end]
        end+=1
    elif total>m:
        total-=arr[start]
        start+=1
    else:
        count+=1
        total-=arr[start]
        start+=1
print(count)