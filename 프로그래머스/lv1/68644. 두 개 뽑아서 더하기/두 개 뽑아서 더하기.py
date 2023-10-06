import itertools

def solution(numbers):
    answer = []
    l=list(itertools.combinations(numbers, 2)) #2개씩 조합
    
    for i in range(len(l)):
        answer.append(sum(l[i]))
        
    answer = list(set(answer)) #중복제거
    answer.sort()  #정렬
    
    return answer
