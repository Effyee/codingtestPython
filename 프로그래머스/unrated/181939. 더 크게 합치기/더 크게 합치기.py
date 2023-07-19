def solution(a, b):
    answer = 0
    str1=str(a)+str(b)
    str2=str(b)+str(a)
    if(int(str1)>int(str2)):
        answer=int(str1)
    else:
        answer=int(str2)
    return answer