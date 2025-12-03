import sys

input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))
p=[0]*(n+1)
p[0]=arr[0]
for i in range(1,n):
    p[i]=p[i-1]+arr[i]
p.insert(0,0)

for _ in range(m):
    start,end=map(int,input().split())
    print(p[end]-p[start-1])