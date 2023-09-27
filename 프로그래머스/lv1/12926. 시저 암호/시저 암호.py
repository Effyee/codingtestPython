def solution(s, n):
    answer = ''
    for char in s:
        if char == ' ':
            # 공백 문자는 그대로 추가
            answer += ' '
        elif char.isupper():
            # 대문자 알파벳 처리
            shifted = ord(char) + n
            if shifted > ord('Z'):
                # 밀린 결과가 'Z'를 넘어가면 다시 'A'부터 시작
                answer += chr(ord('A') + (shifted - ord('Z') - 1))
            else:
                answer += chr(shifted)
        else:
            # 소문자 알파벳 처리
            shifted = ord(char) + n
            if shifted > ord('z'):
                # 밀린 결과가 'z'를 넘어가면 다시 'a'부터 시작
                answer += chr(ord('a') + (shifted - ord('z') - 1))
            else:
                answer += chr(shifted)
    
    return answer

