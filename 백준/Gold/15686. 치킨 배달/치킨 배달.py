import sys
input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

# 집과 치킨집 좌표 뽑기
houses = [(i, j) for i in range(n) for j in range(n) if city[i][j] == 1]
chickens = [(i, j) for i in range(n) for j in range(n) if city[i][j] == 2]

answer = int(1e9)

def get_city_chicken_distance(selected):
    total = 0
    for hx, hy in houses:
        dist = int(1e9)
        for cx, cy in selected:
            dist = min(dist, abs(hx - cx) + abs(hy - cy))
        total += dist

        # 💡 가지치기: 이미 현재 최솟값보다 커지면 더 볼 필요 없음
        if total >= answer:
            return int(1e9)
    return total

def bt(start, selected):
    global answer
    # M개 골랐을 때 도시 치킨 거리 계산
    if len(selected) == m:
        city_dist = get_city_chicken_distance(selected)
        answer = min(answer, city_dist)
        return

    # 조합
    for i in range(start, len(chickens)):
        selected.append(chickens[i])
        bt(i + 1, selected)
        selected.pop()

bt(0, [])
print(answer)
