def solution(name):
    answer = 0
    n = len(name)

    # 알파벳 변경 최소 횟수 계산
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    # 커서 이동 최소 횟수 계산
    min_move = n - 1
    for i in range(n):
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        distance = i + n - next_idx + min(i, n - next_idx)
        min_move = min(min_move, distance)

    answer += min_move
    return answer
