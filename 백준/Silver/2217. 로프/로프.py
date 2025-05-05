import sys
input=sys.stdin.readline

n=int(input())
li=sorted([int(input()) for _ in range(n)],reverse=True)
answer=-int(1e9)

for i in range(n):
    answer=max(answer,li[i]*(i+1))

print(answer)