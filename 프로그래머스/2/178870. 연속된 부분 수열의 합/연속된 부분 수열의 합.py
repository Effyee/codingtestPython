def solution(sequence, k):
    n = len(sequence)
    interval_sum = 0
    right = 0
    INF = int(1e9)
    answer = [-INF, INF]

    for left in range(n):
        while right < n and interval_sum < k:
            interval_sum += sequence[right]
            right += 1

        if interval_sum == k:
            if answer[1] - answer[0] > (right - 1) - left:
                answer = [left, right - 1]

        interval_sum -= sequence[left]

    return answer
