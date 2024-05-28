from collections import defaultdict
def solution(clothes):
    answer = 0
    dic = defaultdict(int)
    for cloth, type in clothes:
        dic[type] += 1

    answer = 1
    for type in dic:
        answer *= (dic[type] + 1) # 각 종류별로 옷을 입는 경우의 수 + 안 입는 경우

    answer -= 1 # 모든 종류에서 아무것도 선택하지 않는 경우 제외
    return answer