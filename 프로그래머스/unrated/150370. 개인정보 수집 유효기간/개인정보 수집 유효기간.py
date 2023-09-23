def calc_date(date):
    year,month,day=map(int,date.split('.'))
    return year*12*28+month*28+day

def solution(today, terms, privacies):
    answer = []
    today_date=calc_date(today)
    term_map={term[0]:int(term[2:]) for term in terms}
    for index,privacy in enumerate(privacies):
        expire=term_map[privacy[-1]]
        date=calc_date(privacy[:-2])+expire*28
        if date<=today_date:
            answer.append(index+1)
    return answer