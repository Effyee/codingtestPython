
def solution(n):
    # 정수 n을 문자열로 변환하여 각 자릿수를 문자열 리스트로 만듭니다.
    digits = list(str(n))
    
    # 문자열 리스트를 정수로 변환하고 내림차순으로 정렬합니다.
    sorted_digits = sorted(map(int, digits), reverse=True)
    
    # 정렬된 정수 리스트를 다시 문자열로 합쳐서 새로운 정수를 생성합니다.
    new_number = int(''.join(map(str, sorted_digits)))
    
    return new_number
