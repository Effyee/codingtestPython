import heapq
import sys
input=sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

A=sorted(A,reverse=True)
heapq.heapify(B)

answer=0
for i in range(n):
    answer+=heapq.heappop(B)*A[i]

print(answer)