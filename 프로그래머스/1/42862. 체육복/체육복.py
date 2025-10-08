def solution(n, lost, reserve):
    real_lost = list(set(lost) - set(reserve))
    real_reserve = list(set(reserve) - set(lost))
    
    answer = n - len(real_lost)  # 처음 체육복 있는 학생 수
    
    for l in sorted(real_lost):
        if l-1 in real_reserve:
            real_reserve.remove(l-1)
            answer += 1
        elif l+1 in real_reserve:
            real_reserve.remove(l+1)
            answer += 1
    
    return answer
