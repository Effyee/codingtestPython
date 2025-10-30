def solution(n, lost, reserve):
    # 서로 겹치는 학생(자기 옷을 잃었지만 여분도 가진 경우) 제거
    new_r = sorted(set(reserve) - set(lost))
    new_l = set(lost) - set(reserve)

    assigned = set()   # 이미 체육복을 받은 학생(중복 수여 방지)
    answer = n - len(new_l)  # 기본으로 옷 있는 학생 수 (reserve 겹친 경우 제거 후)

    for r in new_r:
        if r-1 in new_l and (r-1) not in assigned:
            assigned.add(r-1)
            answer += 1
        elif r+1 in new_l and (r+1) not in assigned:
            assigned.add(r+1)
            answer += 1

    return answer
