N=int(input())
flag=False
for i in range(N):
    l = list(map(int, str(i).rstrip()))
    t=sum(l)+i
    if t==N:
        print(i)
        flag=True
        break

if not flag:
    print(0)