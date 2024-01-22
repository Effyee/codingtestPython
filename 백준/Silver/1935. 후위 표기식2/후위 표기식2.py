import sys
n=int(sys.stdin.readline().rstrip())
expression=sys.stdin.readline().rstrip()
values = [int(input()) for _ in range(n)]

dic={chr(65+i):values[i] for i in range(n)}

def solution(dic):
    stack=[]
    for char in expression:
        if char.isalpha():
            stack.append(dic[char])
        else:
            b=stack.pop()
            a=stack.pop()
            if char=='+':
                stack.append(a+b)
            elif char=='-':
                stack.append(a-b)
            elif char=='*':
                stack.append(a*b)
            else:
                stack.append(a/b)
    print(f"{stack[0]:.2f}")

solution(dic)

