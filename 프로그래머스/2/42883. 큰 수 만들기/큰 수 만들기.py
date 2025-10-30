def solution(number, k):
    answer = ''
    stack=[]
    num=list(map(int,number))
    count=0
    
    for i in range(len(num)):
        while stack and stack[-1]<num[i] and count<k:
            stack.pop()
            count+=1
        stack.append(num[i])
    
    stack=stack[:len(number)-k]
    return ''.join(map(str,stack))