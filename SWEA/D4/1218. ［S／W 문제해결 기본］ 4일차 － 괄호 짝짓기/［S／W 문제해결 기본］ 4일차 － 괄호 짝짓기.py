for _ in range(10):
    n=int(input())
    arr=list(input().strip())

    result=0
    stack=[]
    for i in range(n):
        if arr[i] in ['(','[','{','<']:
            stack.append(arr[i])
        else:
            if not stack:
                break
            elif arr[i]==')':
                if stack[-1]=='(':
                    stack.pop()
                else:
                    break
            elif arr[i]==']':
                if stack[-1]=='[':
                    stack.pop()
                else:
                    break
            elif arr[i]=='}':
                if stack[-1]=='{':
                    stack.pop()
                else:
                    break
            elif arr[i]=='>':
                if stack[-1]=='<':
                    stack.pop()
                else:
                    break
    if not stack:
        result=1

    print(f'#{_+1} {result}')
