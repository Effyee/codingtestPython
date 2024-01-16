n = int(input())
expression = input()
values = [int(input()) for _ in range(n)]

# 피연산자에 해당하는 값을 사전으로 매핑합니다.
operand_values = {chr(65 + i): values[i] for i in range(n)}

stack = []
for char in expression:
    if char.isalpha():  # 피연산자인 경우
        stack.append(operand_values[char])
    else:  # 연산자인 경우
        b = stack.pop()
        a = stack.pop()
        if char == '+':
            stack.append(a + b)
        elif char == '-':
            stack.append(a - b)
        elif char == '*':
            stack.append(a * b)
        elif char == '/':
            stack.append(a / b)

# 결과를 소수점 둘째 자리까지 출력합니다.
print(f"{stack[0]:.2f}")