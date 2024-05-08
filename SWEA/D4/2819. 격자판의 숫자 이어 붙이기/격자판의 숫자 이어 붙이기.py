from collections import deque

tc = int(input())


def bfs(graph):
    answer = set()  
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        for j in range(4):
            q = deque([(i, j, graph[i][j])])  

            while q:
                x, y, num = q.popleft()
                if len(num) == 7:  
                    answer.add(num)  
                    continue

                for k in range(4): 
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < 4 and 0 <= ny < 4: 
                        q.append((nx, ny, num + graph[nx][ny]))  

    return len(answer)  


for t in range(1, tc + 1):
    graph = [input().split() for _ in range(4)]  
    print(f'#{t} {bfs(graph)}')  
