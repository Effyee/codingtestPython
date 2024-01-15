import sys
def solution(s):
    answer = ''
    stack = []
    for char in s:
        if char.isalpha():  # 피연산자인 경우 바로 결과에 추가
            answer += char
        else:
            if char == '(':
                stack.append(char)
            elif char in ['*', '/']:  # '*', '/' 연산자 처리
                while stack and stack[-1] in ['*', '/']:  # 우선순위가 높거나 같은 연산자를 pop
                    answer += stack.pop()
                stack.append(char)
            elif char in ['+', '-']:  # '+', '-' 연산자 처리
                while stack and stack[-1] in ['*', '/', '+', '-']:  # 우선순위가 높거나 같은 연산자를 pop
                    answer += stack.pop()
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':  # '('를 만날 때까지 pop
                    answer += stack.pop()
                stack.pop()  # '(' 제거

    while stack:  # 스택에 남은 연산자를 모두 pop하여 결과에 추가
        answer += stack.pop()
    return answer  # print 대신 return을 사용하여 결과값 반환

s=sys.stdin.readline().rstrip()
print(solution(s))
