import sys

def solution(n,p):
    ans=0
    p.sort()
    for i in range(n):
        ans+=p[i]*(n-i)
    return ans

if __name__=="__main__":
    input=sys.stdin.readline
    n=int(input())
    p=list(map(int,input().split()))
    answer=solution(n,p)
    print(answer)