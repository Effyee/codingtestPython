for _ in range(10):
    n=int(input())

    graph=[list(map(int,input().split())) for _ in range(n)]

    answer=0

    for i in range(n):
        stack=[]
        for j in range(n):
            if graph[j][i]==1:
                stack.append(1)
            elif graph[j][i]==2 and stack:
                    answer+=1
                    stack=[]

    print(f'#{_+1} {answer}')

