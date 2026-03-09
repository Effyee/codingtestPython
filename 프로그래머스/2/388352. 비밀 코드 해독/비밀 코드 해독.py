from itertools import combinations
def solution(n, q, ans):
    answer = 0
    nums=[i for i in range(1,n+1)]
    for i in range(len(ans)):
        if ans[i]==0:
            for num in q[i]:
                if num in nums:
                    nums.remove(num)
                    
    for c in combinations(nums,5):
        flag=True
        for i in range(len(ans)):
            if len(set(c)&set(q[i]))!=ans[i]:
                flag=False
                break
        if flag:
            answer+=1
        
    return answer