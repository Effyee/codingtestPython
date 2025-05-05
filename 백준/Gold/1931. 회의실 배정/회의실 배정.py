import sys
import heapq
input=sys.stdin.readline

#한 개의 회의실
n=int(input())
hq=[]
q=[]
for _ in range(n):
    start,end=map(int,input().split())
    heapq.heappush(hq,(end,start))

answer,time=0,0
while True:
    if len(hq)==0:
        break
    end,start=heapq.heappop(hq)
    if time<=start:
        answer+=1
        time=end
    else:
        continue

print(answer)