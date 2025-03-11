import sys
input=sys.stdin.readline
N=int(input())
stack=[]
for _ in range(N):
    number=int(input())
    if number==0:
        if not stack:
            continue
        else:
            stack.pop()
    else:
        stack.append(number)

print(sum(stack))