from collections import deque

n,k=map(int,input().split())

def solution(n,k):
    answer=[]
    q=deque([i for i in range(1,n+1)])
    while q:
        q.rotate(-(k-1))
        answer.append(str(q.popleft()))


    print("<"+', '.join(answer)+">")


solution(n,k)