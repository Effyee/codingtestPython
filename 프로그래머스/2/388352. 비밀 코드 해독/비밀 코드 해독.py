from itertools import combinations
def solution(n, q, ans):
    answer = 0
    cans=[i for i in range(1,n+1)]
    for i in range(len(q)):
        if ans[i]==0:
            for j in q[i]:
                if j in cans:
                    cans.remove(j)
                
    for c in combinations(cans,5):
        flag=True
        for i in range(len(q)):
            if len(set(c) & set(q[i]))!=ans[i]:
                flag=False
                break
        if flag:
            answer+=1
    return answer