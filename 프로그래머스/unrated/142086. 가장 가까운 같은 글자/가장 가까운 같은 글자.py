def solution(s):
    answer = [-1] * len(s)  # 결과 리스트 초기화

    # 왼쪽부터 오른쪽으로 탐색
    for i in range(len(s)):
        for j in range(i - 1, -1, -1):
            if s[i] == s[j]:
                answer[i] = i - j  # 같은 문자가 나온 위치까지의 거리를 저장
                break  # 가장 가까운 위치를 찾았으므로 더 이상 탐색할 필요가 없음

    return answer