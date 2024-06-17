from collections import defaultdict

def solution(want, number, discount):
    answer=0
    wish = defaultdict(int)
    for i in range(len(want)):
        wish[want[i]]=number[i]
        if want[i] not in discount:
            return 0
    wish=sorted(wish.items())

    dic=defaultdict(int)
    for i in range(len(discount)):
        d=discount[i:i+10]
        dic = defaultdict(int)
        for menu in d:
            dic[menu]+=1
        dic=sorted(dic.items())
        if dic==wish:
            answer+=1
    return answer