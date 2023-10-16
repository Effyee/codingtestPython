def solution(n, lost, reserve):
    # 도난당하면서 여분의 옷도 있는 사람들 처리
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)

    for r in list(set_reserve):
        if r-1 in set_lost:
            set_lost.remove(r-1)
            continue
        if r+1 in set_lost:
            set_lost.remove(r+1)
            
    return n - len(set_lost)
