def solution(name):
    n = len(name)
    
    # 1️⃣ 글자 변경 횟수
    answer = 0
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    
    # 2️⃣ 커서 이동 최소값 계산
    move = n - 1  # 기본: 오른쪽으로 쭉 이동
    for i in range(n):
        next_i = i + 1
        # 연속된 'A' 건너뛰기
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        # i까지 오른쪽, 뒤쪽으로 돌아가는 경우 최소값 계산
        distance = min(i*2 + n - next_i, (n - next_i)*2 + i)
        move = min(move, distance)
    
    answer += move
    return answer
