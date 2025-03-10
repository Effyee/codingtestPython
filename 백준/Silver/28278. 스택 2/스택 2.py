import sys

input = sys.stdin.readline

N = int(input().strip())  # 개행 문자 제거
stack = []

for _ in range(N):
    s = input().split()  # 공백을 기준으로 나누기
    command = int(s[0])  # 첫 번째 값은 명령어

    if command == 1:
        stack.append(int(s[1]))  # 숫자 추가
    elif command == 2:
        print(stack.pop() if stack else -1)  # pop 후 출력, 비었으면 -1
    elif command == 3:
        print(len(stack))  # 스택 크기 출력
    elif command == 4:
        print(1 if not stack else 0)  # 비었으면 1, 아니면 0 출력
    elif command == 5:
        print(stack[-1] if stack else -1)  # 맨 위 값 출력, 없으면 -1
