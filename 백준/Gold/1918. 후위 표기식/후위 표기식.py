import sys

def solution(s):
    answer = ''
    stack = []
    for char in s:
        if char.isalpha():  # 알파벳인 경우 출력
            answer += char
        else:
            if char == '(':  # 여는 괄호는 스택에 푸시
                stack.append(char)
            elif char in ['*', '/']:  # *, / 연산자 처리
                while stack and stack[-1] in ['*', '/']:
                    answer += stack.pop()
                stack.append(char)
            elif char in ['+', '-']:  # +, - 연산자 처리
                while stack and stack[-1] in ['*', '/', '+', '-']:
                    answer += stack.pop()
                stack.append(char)
            elif char == ')':  # 닫는 괄호를 만나면 여는 괄호가 나올 때까지 스택을 팝
                while stack and stack[-1] != '(':
                    answer += stack.pop()
                stack.pop()  # 여는 괄호를 팝하여 제거
    while stack:  # 스택에 남은 연산자를 모두 팝하여 추가
        answer += stack.pop()
    print(answer)

s = sys.stdin.readline().rstrip()
solution(s)
