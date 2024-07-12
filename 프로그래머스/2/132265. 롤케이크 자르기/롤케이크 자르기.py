from collections import Counter
def solution(topping):
    answer = 0
    left_count = Counter()
    right_count = Counter(topping)
    left_varieties = 0
    right_varieties = len(right_count)

    for i in range(len(topping)):
        # 현재 토핑을 왼쪽으로 이동
        if left_count[topping[i]] == 0:
            left_varieties += 1
        left_count[topping[i]] += 1

        # 현재 토핑을 오른쪽에서 제거
        right_count[topping[i]] -= 1
        if right_count[topping[i]] == 0:
            right_varieties -= 1

        # 토핑의 종류가 같으면 answer 증가
        if left_varieties == right_varieties:
            answer += 1

    return answer