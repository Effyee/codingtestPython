def solution(n, q, ans):
    answer = 0
    nums = [True] * (n + 1)

    # ans == 0 인 숫자 제거
    for i in range(len(q)):
        if ans[i] == 0:
            for x in q[i]:
                nums[x] = False

    def check(li):
        li_set = set(li)
        for i in range(len(q)):
            if len(set(q[i]) & li_set) != ans[i]:
                return False
        return True

    def backtrack(start, li):
        nonlocal answer

        if len(li) == 5:
            if check(li):
                answer += 1
            return

        for num in range(start, n + 1):
            if nums[num]:
                li.append(num)
                backtrack(num + 1, li)
                li.pop()

    backtrack(1, [])
    return answer
