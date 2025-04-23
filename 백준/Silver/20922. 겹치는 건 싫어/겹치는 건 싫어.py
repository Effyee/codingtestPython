import sys
from collections import defaultdict
input=sys.stdin.readline

n,k=map(int,input().split())
arr=list(map(int,input().split()))

start,end=0,0
dict=defaultdict(int)
answer=-1

while end<n:
    if dict[arr[end]]<k:
        dict[arr[end]]+=1
        end+=1
    else:
        dict[arr[start]]-=1
        start+=1

    answer = max(answer, end-start)

print(answer)