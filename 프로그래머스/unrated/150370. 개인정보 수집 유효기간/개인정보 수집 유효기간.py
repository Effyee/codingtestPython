def calc_date(today):
    year, month, day = map(int, today.split("."))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    answer = []
		# 오늘 날짜 계산
    today_date = calc_date(today)
		# 약관 매핑
    term_map = {term[0]: int(term[2:]) for term in terms}
    # 만료일과 오늘 날짜 비교
    for index, privacy in enumerate(privacies):
        expire = term_map[privacy[-1]]
        date = calc_date(privacy[:-2]) + expire * 28
        if date <= today_date:
            answer.append(index + 1)
    return answer