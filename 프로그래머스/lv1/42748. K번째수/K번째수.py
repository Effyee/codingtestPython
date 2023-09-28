def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        sub_array = array[i-1:j] # python의 인덱싱은 0부터 시작합니다.
        sub_array.sort()
        answer.append(sub_array[k-1]) # k번째 숫자를 찾습니다.
    return answer

