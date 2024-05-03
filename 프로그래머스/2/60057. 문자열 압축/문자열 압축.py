def solution(s):
    answer = len(s)  # 최소 길이를 초기 문자열 길이로 설정
    for i in range(1, len(s)//2 + 1):  # 1부터 시작하여 절반 길이까지
        l = cutted_list(s, i)
        compressed = make_news(l)
        answer = min(answer, len(compressed))  # 가장 짧은 길이로 업데이트
    return answer

def cutted_list(s, n):
    l = []
    for i in range(0, len(s), n):
        l.append(s[i:i+n])
    return l

def make_news(l):
    new_s = ''
    cnt = 1
    for i in range(1, len(l)):
        if l[i-1] != l[i]:
            if cnt == 1:  # 반복되지 않는 경우, 숫자를 붙이지 않음
                new_s += l[i-1]
            else:
                new_s += str(cnt) + l[i-1]
            cnt = 1
        else:
            cnt += 1
    # 마지막으로 남은 문자열 처리
    if cnt == 1:
        new_s += l[-1]
    else:
        new_s += str(cnt) + l[-1]
    return new_s


