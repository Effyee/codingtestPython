def solution(s):
    words = s.split(' ')
    answer = ''
    for word in words:
        for i in range(len(word)):
            if word[i]==' ':
                answer+=' '
            elif i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += ' '
    return answer[:-1] # 마지막에 추가된 공백 제거

