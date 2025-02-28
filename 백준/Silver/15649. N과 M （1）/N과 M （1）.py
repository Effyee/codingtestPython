n, m = map(int, input().split())

answer = []
visited = [False] * (n + 1) 


def backtrack():
    if len(answer) == m:
        print(" ".join(map(str, answer)))  
        return

    for i in range(1, n + 1):  
        if not visited[i]:  
            visited[i] = True  
            answer.append(i)  
            backtrack()  
            answer.pop() 
            visited[i] = False  


backtrack()
