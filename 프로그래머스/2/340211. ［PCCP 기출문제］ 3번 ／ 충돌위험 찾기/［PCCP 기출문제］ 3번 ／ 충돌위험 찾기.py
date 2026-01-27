from collections import defaultdict

def solution(points, routes):
    answer = 0
    time_location = defaultdict(list)

    for route in routes:
        time = 0
        x, y = points[route[0]-1]
        time_location[0].append((x, y))  # 시작 위치 기록

        for i in range(len(route) - 1):
            nx, ny = points[route[i+1]-1]

            # r 먼저 이동
            while x != nx:
                x += 1 if nx > x else -1
                time += 1
                time_location[time].append((x, y))

            # c 이동
            while y != ny:
                y += 1 if ny > y else -1
                time += 1
                time_location[time].append((x, y))
    for t in time_location:
        counter = defaultdict(int)
        for pos in time_location[t]:
            counter[pos] += 1
        for cnt in counter.values():
            if cnt >= 2:
                answer += 1
    return answer
