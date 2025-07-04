while True:
    s = input()
    if s == '.':
        break

    stack = []
    balanced = True
    for c in s:
        if c in '([':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] != '(':
                balanced = False
                break
            stack.pop()
        elif c == ']':
            if not stack or stack[-1] != '[':
                balanced = False
                break
            stack.pop()

    if balanced and not stack:
        print('yes')
    else:
        print('no')
