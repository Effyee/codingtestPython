def solution(n):
    standard=str(bin(n)).count('1')
    l=0
    while l!=standard:
        n+=1
        l=str(bin(n)).count('1')
    return n
