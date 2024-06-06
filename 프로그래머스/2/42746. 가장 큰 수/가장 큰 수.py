def solution(numbers):
    answer = ''
    numbers_str = list(map(str, numbers))
    numbers_str.sort(key=lambda x: x * 3, reverse=True)
    answer=int(''.join(numbers_str))
    return str(answer)