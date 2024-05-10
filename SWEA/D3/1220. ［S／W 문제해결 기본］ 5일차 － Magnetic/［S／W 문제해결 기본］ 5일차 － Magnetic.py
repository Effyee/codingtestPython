for _ in range(10):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    for i in range(n):
        stack = []
        for j in range(n):
            if graph[j][i] == 1:
                stack.append(1)
            elif graph[j][i] == 2 and stack: # S극 자성체를 만나고, 스택이 비어 있지 않다면(즉, N극 자성체가 있었다면)
                answer += 1 # 교착 상태 개수 증가
                stack = [] # 스택 초기화
    print(f'#{_+1} {answer}')
