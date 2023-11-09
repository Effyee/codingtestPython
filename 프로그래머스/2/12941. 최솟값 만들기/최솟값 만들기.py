def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        multiplication=A[i]*B[i]
        answer+=multiplication
    return answer