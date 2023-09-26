from itertools import combinations

def solution(phoneBook):
    answer=0
    list_number= combinations(phoneBook, 3)
    print(list_number)
    for l in list_number:
        if sum(list(l))==0:
            answer+=1
    return answer
  