for _ in range(10):
    tc=int(input())
    graph=[list(map(int,input().split())) for _ in range(100)]

    row,col,dia1,dia2=0,0,0,0
    for i in range(100):
        tmp_row=sum(graph[i])
        row=max(row,tmp_row)
        dia1+=graph[i][i]
        dia2+=graph[100-i-1][i]
        tmp_col=0
        for j in range(100):
            tmp_col+=graph[j][i]
            col=max(col,tmp_col)

    print(f'#{_+1} {max(row,col,dia1,dia2)}')


