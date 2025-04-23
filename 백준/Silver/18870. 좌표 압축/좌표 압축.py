import sys
from collections import defaultdict
input=sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))
sorted_li=sorted(li)
dict=defaultdict(int)
ans=[]
idx=1
for i in range(len(sorted_li)):
    if dict[sorted_li[i]]>0:
        continue
    else:
        dict[sorted_li[i]]=idx
        idx+=1

for num in li:
    ans.append(dict[num]-1)

print(' '.join(map(str,ans)))