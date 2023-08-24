def solution(absolutes, signs):
    # signs가 참이면 해당 absolutes의 수가 양수, 거짓이면 음수
    # 주어진 수를 하나씩 접근
    # 양수, 음수가 적용된 실제 합
    answer = 0
    for i in range(len(absolutes)):
        #  참인경우 양수이므로 더하기
        if signs[i]:
            answer += absolutes[i]
        # 거짓인 경우 음수이므로 빼기
        else:
            answer -= absolutes[i]
    return answer