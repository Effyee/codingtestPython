def solution(n, results):
    answer = 0
    graph=[[0]*(n) for _ in range(n)]
    
    for result in results:
        a,b=result
        graph[a-1][b-1]=1
        graph[b-1][a-1]=-1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j and graph[i][j] in [1,-1]:
                    continue
                if graph[i][k]==graph[k][j]==1:
                    graph[i][j]=1
                    graph[j][k]=graph[k][i]=graph[j][i]=-1
    for row in range(n):
        if graph[row].count(0)==1:
            answer+=1
        
    return answer