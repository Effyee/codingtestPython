def solution(number, k):
    stack = []  # 숫자를 저장할 스택
    for num in number:
        # 스택이 비어있지 않고, k가 0보다 크며, 스택의 마지막 원소가 현재 숫자보다 작을 때
        while stack and k > 0 and stack[-1] < num:
            stack.pop()  # 스택의 마지막 원소 제거
            k -= 1  # 제거할 숫자 개수 감소
        stack.append(num)  # 현재 숫자를 스택에 추가

    # k가 0보다 크면(아직 제거할 숫자가 남아있으면) 스택의 끝에서 k개의 숫자 제거
    if k > 0:
        stack = stack[:-k]
    return ''.join(stack)
