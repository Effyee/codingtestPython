def solution(expression):
    answer = 0
    
    def make_ex(expression):
        expression=list(expression)
        stack=[]
        num=''
        for e in expression:
            if e in ['0','1','2','3','4','5','6','7','8','9']:
                num+=e
            else:
                stack.append(int(num))
                num=''
                stack.append(e)
        stack.append(int(num))
        return stack
                
    stack=make_ex(expression)
    
    def calculate(tokens, priority):
        tokens = tokens[:]  # 원본 보호 (중요)

        for op in priority:
            new = []
            i = 0
            while i < len(tokens):
                if tokens[i] == op:
                    # 직전 숫자 + 다음 숫자 계산
                    prev = new.pop()
                    next_ = tokens[i+1]

                    if op == '+':
                        new.append(prev + next_)
                    elif op == '-':
                        new.append(prev - next_)
                    elif op == '*':
                        new.append(prev * next_)

                    i += 2  # 숫자 하나 더 먹었으니까
                else:
                    new.append(tokens[i])
                    i += 1
            tokens = new  # 줄어든 리스트로 교체

        return abs(tokens[0])

    
    ex=['+','-','*']
    visited=[False]*3
    def permute(priority):
        nonlocal answer
        if len(priority)==3:
            result = calculate(stack, priority)
            answer = max(answer, result)
            return
        for i in range(3):
            if not visited[i]:
                priority.append(ex[i])
                visited[i]=True
                permute(priority)
                priority.pop()
                visited[i]=False
        return 
    permute([])
    return answer