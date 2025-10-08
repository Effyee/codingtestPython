def solution(number, k):
    num = list(map(int, number))
    stack = []
    cnt = 0
    for n in num:
        while stack and cnt < k and stack[-1] < n:
            stack.pop()
            cnt += 1
        stack.append(n)
    # 남은 제거
    while cnt < k:
        stack.pop()
        cnt += 1
    return ''.join(map(str, stack))
