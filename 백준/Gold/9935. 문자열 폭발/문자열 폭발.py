import sys
input=sys.stdin.readline

s = input().strip()
bomb = input().strip()
bomb_len = len(bomb)

stack = []
for char in s:
    stack.append(char) # 문자를 스택에 추가
    # 스택의 끝 부분이 bomb과 일치하는지 확인
    if len(stack) >= bomb_len and "".join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len): # bomb 길이만큼 스택에서 pop
            stack.pop()

result = "".join(stack)
print(result if result else "FRULA")