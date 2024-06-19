def solution(n, left, right):
    result = []
    for index in range(left, right + 1):
        i = index // n  # 행
        j = index % n   # 열
        result.append(max(i, j) + 1)
    return result