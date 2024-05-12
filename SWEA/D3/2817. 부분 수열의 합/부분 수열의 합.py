def dfs(result,cnt):
    global answer
    if result==K:
        answer+=1
        return
    if cnt==N:
        return

    dfs(result+numbers[cnt],cnt+1)
    dfs(result,cnt+1)

T=int(input())

for _ in range(T):
    #N(수의 개수),K(결과값)
    N,K=map(int,input().split())
    numbers=list(map(int,input().split()))

    answer=0
    dfs(0,0)

    print(f'#{_+1} {answer}')


