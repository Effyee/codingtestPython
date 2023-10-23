import itertools

def solution(nums):
    answer = 0
    
    # 가능한 모든 세 숫자 조합을 생성하고 각각의 합계 계산
    sums = [sum(combination) for combination in itertools.combinations(nums,3)]
    
    # 각 합계에 대해 소수인지 확인 
    for num_sum in sums:
        is_prime = True

        # num_sum을 sqrt(num_sum)까지의 모든 숫자로 나눠보기 (소수 판정)
        for j in range(2, int(num_sum ** (0.5)) + 1):
            if num_sum % j == 0:   # 만약 나눠진다면 해당 숫자는 소수가 아님.
                is_prime = False   
                break
        
        # 위 반복문에서 한 번도 나눠진 적 없다면 해당 숫자는 소수.
        if is_prime:  
            answer += 1
    
    return answer 
