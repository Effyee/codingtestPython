for _ in range(10):
    n=int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]

    row, col = 0, 0
    dia1, dia2 = 0, 0  # 두 대각선의 합을 저장할 변수
    for i in range(100):
        row = max(row, sum(graph[i]))  # 각 행의 합 중 최대값
        dia1 += graph[i][i]  # 주 대각선 합
        dia2 += graph[i][99-i]  # 부 대각선 합

        tmp_col = sum(graph[j][i] for j in range(100))  # 각 열의 합
        col = max(col, tmp_col)  # 각 열의 합 중 최대값

    answer = max(row, col, dia1, dia2)  # 행, 열, 두 대각선의 합 중 최대값

    print(f"#{_+1} {answer}")

