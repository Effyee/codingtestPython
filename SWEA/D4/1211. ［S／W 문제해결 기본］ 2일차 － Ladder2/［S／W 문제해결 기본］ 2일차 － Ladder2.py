def ladder_game(graph, y):
    x = 0
    move_count = 0  # 이동 횟수를 저장할 변수
    while x < 99:  # x가 99보다 작은 동안 반복
        # 오른쪽으로 이동 가능한지 확인
        if y < 99 and graph[x][y+1] == 1:  # y가 99보다 작고, 오른쪽이 1일 때
            while y < 99 and graph[x][y+1] == 1:  # 범위를 벗어나지 않고, 오른쪽이 1일 동안
                y += 1  # 오른쪽으로 이동
                move_count += 1  # 이동 횟수 증가
            x += 1  # 아래로 이동
            move_count += 1  # 이동 횟수 증가
        # 왼쪽으로 이동 가능한지 확인
        elif y > 0 and graph[x][y-1] == 1:  # y가 0보다 크고, 왼쪽이 1일 때
            while y > 0 and graph[x][y-1] == 1:  # 범위를 벗어나지 않고, 왼쪽이 1일 동안
                y -= 1  # 왼쪽으로 이동
                move_count += 1  # 이동 횟수 증가
            x += 1  # 아래로 이동
            move_count += 1  # 이동 횟수 증가
        else:
            x += 1  # 양쪽 모두 이동할 수 없을 때, 아래로 이동
            move_count += 1  # 이동 횟수 증가
    return move_count  # 이동 횟수 반환

# 입력 받기 및 결과 출력
for _ in range(10):  # 테스트 케이스 수가 10개라고 가정
    tc = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    min_move = float('inf')  # 가장 작은 이동 횟수를 저장할 변수
    result = 0  # 결과를 저장할 변수
    for i in range(100):
        if graph[0][i] == 1:
            move_count = ladder_game(graph, i)
            if move_count <= min_move:  # 최소 이동 횟수보다 작거나 같은 경우
                min_move = move_count  # 최소 이동 횟수 업데이트
                result = i  # 결과 업데이트
    print(f"#{tc} {result}")  # 결과 출력
