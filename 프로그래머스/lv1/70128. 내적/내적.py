def solution(a, b):
    answer = 0
    
    for a_val, b_val in zip(a, b):
        answer += a_val * b_val
    
    return answer