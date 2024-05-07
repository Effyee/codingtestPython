def dfs(n):
    global answer
    if N==n:
        answer=max(answer,int(''.join(map(str,lst))))
        return
    for i in range(L-1):
        for j in range(i+1,L):
            lst[i],lst[j]=lst[j],lst[i]

            chk=int(''.join(map(str,lst)))
            if (n,chk) not in v:
                v.append((n,chk))
                dfs(n+1)
   
            lst[j],lst[i]=lst[i],lst[j]


t=int(input())

for _ in range(t):
    numbers,n=input().split()

    N=int(n)

    lst,v=[],[]

    for number in numbers:
        lst.append(int(number))

    L=len(lst)
    answer=0
    dfs(0)

    print(f'#{_+1} {answer}')