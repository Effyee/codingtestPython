import sys
input=sys.stdin.readline

n,m=map(int,input().split())
nums=sorted(list(map(int,input().split())))

visited=[False]*len(nums)
answer=[]

def backtrack():
    global answer
    if len(answer)==m:
        print(' '.join(map(str,answer)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i]=True
            answer.append(nums[i])
            backtrack()
            visited[i]=False
            answer.pop()

    return

backtrack()
