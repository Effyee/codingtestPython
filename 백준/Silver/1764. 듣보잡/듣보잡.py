import sys
from collections import defaultdict
input=sys.stdin.readline

n,m=map(int,input().split())
d=defaultdict(int)

for _ in range(n):
    name=input().strip()
    d[name]+=1

for _ in range(m):
    name = input().strip()
    d[name] += 1
answer,li=0,[]
for name in d.keys():
    if d[name]==2:
        answer+=1
        li.append(name)

li.sort()
print(answer)
for name in li:
    print(name)