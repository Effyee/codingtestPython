import sys
input=sys.stdin.readline

n=int(input())
waters=list(map(int,input().split()))
ans=int(1e9)
left,right=0,n-1

while left<right:
    summation = waters[left] + waters[right]
    if abs(summation)<abs(ans):
        ans=summation

    if summation==0:
        break
    elif summation>0:
        right-=1
    else:
        left+=1

print(ans)