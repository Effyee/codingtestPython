from collections import defaultdict

def solution(orders, course):
    answer = []
    menus = defaultdict(int)

    def combi(order, li, c, idx):
        if len(li) == c:
            menus[li] += 1
            return

        for i in range(idx, len(order)):
            combi(order, li + order[i], c, i + 1)

    #주문별 조합 만들기
    for order in orders:
        order = ''.join(sorted(order))   #정렬
        for c in course:
            if len(order) >= c:          
                combi(order, '', c, 0)

    #코스 길이별 최대 주문 횟수 구하기
    max_count = defaultdict(int)
    for menu, cnt in menus.items():
        length = len(menu)
        if length in course and cnt >= 2:
            max_count[length] = max(max_count[length], cnt)

    #최대 횟수에 해당하는 메뉴만 answer에 추가
    for menu, cnt in menus.items():
        length = len(menu)
        if length in course and cnt >= 2 and cnt == max_count[length]:
            answer.append(menu)

    answer.sort()
    return answer
