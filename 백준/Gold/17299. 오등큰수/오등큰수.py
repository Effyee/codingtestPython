import sys
input=sys.stdin.readline

n=int(input())
l=list(map(int,input().split()))
count=[0]*(max(l)+1)
answer=[-1]*(n)

for i in range(n):
    count[l[i]]+=1

stack=[]
for i in range(n):
    while stack and count[l[i]]>count[l[stack[-1]]]:
        answer[stack.pop()]=l[i]
    stack.append(i)
print(*answer)