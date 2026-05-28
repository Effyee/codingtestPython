def solution(park, routes):

    # 문자열 -> 2차원 리스트
    p = [list(row) for row in park]

    # 시작 위치 찾기
    x, y = 0, 0

    for i in range(len(p)):
        for j in range(len(p[0])):
            if p[i][j] == 'S':
                x, y = i, j

    # 방향 설정
    dir_map = {
        'E': (0, 1),
        'W': (0, -1),
        'S': (1, 0),
        'N': (-1, 0)
    }

    # 명령 수행
    for route in routes:

        direction, count = route.split()
        count = int(count)

        dx, dy = dir_map[direction]

        # 현재 위치 저장
        nx, ny = x, y

        # 이동 가능한지 확인
        possible = True

        for _ in range(count):

            nx += dx
            ny += dy

            # 범위 밖 체크
            if nx < 0 or ny < 0 or nx >= len(p) or ny >= len(p[0]):
                possible = False
                break

            # 장애물 체크
            if p[nx][ny] == 'X':
                possible = False
                break

        # 이동 가능하면 최종 위치 반영
        if possible:
            x, y = nx, ny

    return [x, y]