def solution(number, limit, power):
    answer = 0
    divisors = [1] * (number + 1) # 모든 수는 최소 1개(자기 자신)의 약수를 가짐

    for i in range(2, number + 1):
        for j in range(i, number + 1, i): # 배수들을 증가시켜 나감
            divisors[j] += 1
    
    for divisor in divisors[1:]:
        if divisor <= limit:
            answer += divisor
        else:
            answer += power
            
    return answer
