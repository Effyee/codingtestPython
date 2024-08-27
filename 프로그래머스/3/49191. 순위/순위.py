def solution(n, results):
    answer = 0
    graph = [[0]*n for _ in range(n)]

    for result in results:
        player1, player2 = result
        graph[player1-1][player2-1] = 1  # player1이 player2를 이김
        graph[player2-1][player1-1] = -1  # player2가 player1에게 진다

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or graph[i][j] in [1, -1]:
                    continue
                if graph[i][k] == 1 and graph[k][j] == 1:
                    # i가 k를 이기고 k가 j를 이긴 경우
                    graph[i][j] = 1  # i가 j를 이김
                    graph[j][i] = -1  # j가 i에게 짐

    for row in graph:
        if row.count(0) == 1:
            answer += 1
    return answer