def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n

    while left < right:
        mid = (left + right) // 2

        people = 0
        for time in times:
            people += mid // time

        if people >= n:
            right = mid  # 처리 인원이 n 이상이면 시간을 줄이기
        else:
            left = mid + 1  # 처리 인원이 n 미만이면 시간을 늘리기

    return left  # left와 right가 만나는 지점이 최소 시간