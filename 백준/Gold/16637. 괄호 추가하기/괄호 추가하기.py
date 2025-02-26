def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def backtrack(index, current_value):
    global max_result

    # 모든 연산을 다 수행한 경우 최댓값 갱신
    if index >= len(operators):
        max_result = max(max_result, current_value)
        return

    # 1. 괄호를 사용하지 않고 현재 숫자를 연산
    next_value = calculate(current_value, operators[index], numbers[index + 1])
    backtrack(index + 1, next_value)

    # 2. 괄호를 사용해서 다음 연산을 먼저 수행
    if index + 1 < len(operators):
        bracket_value = calculate(numbers[index + 1], operators[index + 1], numbers[index + 2])
        next_value = calculate(current_value, operators[index], bracket_value)
        backtrack(index + 2, next_value)

# 입력 처리
N = int(input().strip())
expression = input().strip()

# 숫자와 연산자를 분리
numbers = []
operators = []

for i in range(N):
    if i % 2 == 0:
        numbers.append(int(expression[i]))
    else:
        operators.append(expression[i])

# 백트래킹 수행
max_result = -float('inf')
backtrack(0, numbers[0])

# 결과 출력
print(max_result)
