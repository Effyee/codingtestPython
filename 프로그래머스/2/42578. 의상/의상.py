from collections import defaultdict

def solution(clothes):
    answer = 1
    types=[]
    l=defaultdict(int)
    for c in clothes:
        cloth,type=c
        l[type] += 1
        if type not in types:
            types.append(type)
    
    for t in types:
        answer*=(l[t]+1)
    return answer-1