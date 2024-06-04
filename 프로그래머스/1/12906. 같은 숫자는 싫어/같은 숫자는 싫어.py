def solution(arr):
    stack=[]
    for a in arr:
        if not stack:
            stack.append(a)
        else:
            if stack[-1]!=a:
                stack.append(a)
    return stack