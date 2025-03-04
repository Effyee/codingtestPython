import sys
input=sys.stdin.readline

N,M=map(int,input().split())

visited=[False]*(N+1)
answer=[]
def backtrack():
    if len(answer)==M:
        print(' '.join(map(str,answer)))
        return

    for i in range(1,N+1):
        if not visited[i]:
            visited[i]=True
            answer.append(i)
            backtrack()
            visited[i]=False
            answer.pop()


backtrack()