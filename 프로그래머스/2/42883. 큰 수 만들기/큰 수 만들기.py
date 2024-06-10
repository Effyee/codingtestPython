def solution(number, k):
    number=list(map(int,number))

    stack=[]
    cnt=0
    for i in range(len(number)):
        if not stack:
            stack.append(number[i])
        else:
            while stack and stack[-1]<number[i] and cnt<k:
                stack.pop()
                cnt+=1
            stack.append(number[i])
    if len(stack)>len(number)-k:
        stack=stack[:len(number)-k]

    return ''.join(map(str,stack))