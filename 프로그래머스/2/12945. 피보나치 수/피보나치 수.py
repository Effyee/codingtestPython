def solution(n):
    if n==0:
        return 0
    if n==1:
         return 1
    a=0
    b=1
    for i in range(1,n):
        a,b=b,(a+b)%1234567
    return b