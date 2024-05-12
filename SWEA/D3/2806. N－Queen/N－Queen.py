def NQueen(x):
    global result
    if x==n:
        result+=1
        return
    for i in range(n):
        row[x] = i
        if check(x):
            NQueen(x+1)


def check(x):
    for i in range(x):
        if row[x]==row[i] or abs(x-i)==abs(row[x]-row[i]):
            return False
    return True

T=int(input())


for _ in range(T):
    n=int(input())
    row=[0]*(n)
    result=0
    NQueen(0)
    print(f'#{_+1} {result}')
