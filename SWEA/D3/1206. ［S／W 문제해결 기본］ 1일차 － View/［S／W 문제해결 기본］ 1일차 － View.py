def find_max(building):
    idx = 0
    for i in range(1, 5):
        if building[idx] < building[i]:
            idx = i
    return idx

for _ in range(10):
    answer = 0
    n = int(input())
    buildings = list(map(int, input().split()))

    for i in range(n - 4):
        building = buildings[i:i+5]
        if find_max(building) == 2:
            m = building[2]
            sorted_building = sorted(building)
            result = m - sorted_building[-2]
            answer += result

    print(f'#{_+1} {answer}')
