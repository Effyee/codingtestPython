import sys
n = int(sys.stdin.readline())

tops = list(map(int, sys.stdin.readline().split()))  # 탑의 높이를 입력받아 리스트로 저장

stack = []
answer = []

for i in range(n):
    while stack and stack[-1][1] < tops[i]:
        stack.pop()
    if stack:
        answer.append(str(stack[-1][0] + 1))  # 탑의 번호는 1부터 시작하므로 +1
    else:
        answer.append('0')
    stack.append((i, tops[i]))  # 스택에는 탑의 인덱스와 높이를 함께 저장

print(' '.join(answer))
