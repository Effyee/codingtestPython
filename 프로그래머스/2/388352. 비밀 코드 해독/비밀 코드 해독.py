from itertools import combinations
def solution(n, q, ans):
    answer = 0
    numbers=[i for i in range(1,n+1)]
    for c in combinations(numbers,5):
        flag=True
        for i in range(len(q)):
            if(len(set(q[i])&set(c))!=ans[i]):
                flag=False
                break
        if(flag):
            answer+=1
    return answer