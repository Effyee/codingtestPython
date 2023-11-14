def solution(s):
    c1 = 0  # 이진 변환 횟수
    c2 = 0  # 제거된 0의 개수

    while s != '1':
        c1 += 1
        removed_zeros = s.count('0')  # 제거될 0의 개수
        c2 += removed_zeros
        s = bin(s.count('1'))[2:]  # 0 제거 후 길이를 이진수로 변환

    return [c1, c2]
