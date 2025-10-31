import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))

def lower_bound(li,x):
    start,end=0,len(li)-1
    ans=len(li)
    while start<=end:
        mid=(start+end)//2
        if li[mid]>=x:
            ans=mid
            end=mid-1
        else:
            start=mid+1
    return ans

li=[]
for num in arr:
    pos=lower_bound(li,num)
    if pos==len(li):
        li.append(num)
    else:
        li[pos]=num
print(len(li))