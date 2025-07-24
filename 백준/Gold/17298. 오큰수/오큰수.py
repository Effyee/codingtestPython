import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
stack=[]
answer=[-1]*n

for i in range(n):
    if not stack:
        stack.append(i)
    else:
        if arr[i]<arr[stack[-1]]:
            stack.append(i)
        else:
            while stack and arr[i]>arr[stack[-1]]:
                answer[stack.pop()]=arr[i]
            stack.append(i)

print(*answer)