import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))
prefix=[0]*(n+1)
prefix[1]=arr[0]
for i in range(2,n+1):
    prefix[i]=arr[i-1]+prefix[i-1]

for _ in range(m):
    s,e=map(int,input().split())
    print(prefix[e]-prefix[s-1])
