import sys
input=sys.stdin.readline

# 배열의 크기: n
n=int(input())
#
k=int(input())
start=1
end=k
answer=0
while start<=end:
    mid=(start+end)//2

    temp=0
    for i in range(1,n+1):
        temp+=min(n,mid//i)

    if temp<k:
         start=mid+1
    else:
        answer=mid
        end=mid-1

print(answer)