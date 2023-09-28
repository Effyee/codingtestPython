def make_binary(n, num):
    binary = ''
    for _ in range(n):
        if num % 2 == 1:
            binary += '#'
        else:
            binary += ' '
        num //= 2
    return binary[::-1] # 거꾸로 뒤집어줍니다.


def solution(n, arr1, arr2):
    answer = []
    
    for a,b in zip(arr1,arr2):
        num = a | b
        answer.append(make_binary(n, num))
    
    return answer
