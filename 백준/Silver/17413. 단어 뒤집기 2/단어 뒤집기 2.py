s = input().strip()
answer = ''
tag = False  # 현재 태그 내부인지 여부
word = ''  # 뒤집을 단어 저장

for letter in s:
    if letter == '<':  # 태그 시작
        if word:  # 이전에 쌓인 단어가 있다면 뒤집어서 추가
            answer += word[::-1]
            word = ''
        tag = True
        answer += letter
    elif letter == '>':  # 태그 종료
        tag = False
        answer += letter
    elif tag:  # 태그 내부
        answer += letter
    else:  # 태그 외부 (단어 또는 공백 처리)
        if letter == ' ':
            answer += word[::-1] + ' '  # 단어 뒤집고 공백 추가
            word = ''
        else:
            word += letter  # 단어 추가

# 마지막 남은 단어 뒤집기
if word:
    answer += word[::-1]

print(answer)
