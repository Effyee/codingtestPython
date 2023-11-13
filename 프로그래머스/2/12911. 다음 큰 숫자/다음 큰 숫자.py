def solution(n):
    count_n = bin(n).count('1')  # n의 2진수에서 1의 갯수를 센다.
    for m in range(n+1, 1000001):  # n보다 큰 수들에 대해
        if bin(m).count('1') == count_n:  # 1의 갯수가 같으면
            return m  # 그 수를 반환한다.
    return -1  # 만약 이런 수가 없다면 -1 반환
