def solution(n, q, ans):
    answer = 0
    def check(li):
        for i in range(len(q)):
            if len(set(li)&set(q[i]))!=ans[i]:
                return False
        return True
    
    def backtrack(idx,li):
        nonlocal answer
        if len(li)==5:
            if check(li):
                answer+=1
            return
        if idx==n+1:
            return
        for i in range(idx,n+1):
            li.append(i)
            backtrack(i+1,li)
            li.pop()
        return
    
    backtrack(1,[])
    
    return answer