T=int(input())

for _ in range(T):
    N=int(input())
    l=list(map(int,input().split()))
    print(min(l),max(l))