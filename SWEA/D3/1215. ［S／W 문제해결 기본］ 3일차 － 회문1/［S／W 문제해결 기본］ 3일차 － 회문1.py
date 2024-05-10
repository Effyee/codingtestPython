for _ in range(10):
    l = int(input())
    graph = [list(input().strip()) for _ in range(8)]

    answer = 0

    # 가로 방향 회문 검사
    for i in range(8):
        for j in range(8 - l + 1):
            horizontal_string = ''.join(graph[i][j:j + l])
            if horizontal_string == horizontal_string[::-1]:  # 회문인지 확인
                answer += 1

    # 세로 방향 회문 검사
    for j in range(8):
        for i in range(8 - l + 1):
            vertical_string = ''.join(graph[k][j] for k in range(i, i + l))
            if vertical_string == vertical_string[::-1]:  # 회문인지 확인
                answer += 1

    print(f'#{_+1} {answer}')
