from collections import Counter

def solution(X, Y):
    # 숫자 개수 세기
    nums = Counter(X) & Counter(Y)
    if not nums: return '-1' # 공통 없는 경우
    elif list(nums) == ['0']: return '0' # 0만 공통인 경우
    
    nums_order = sorted(list(nums),reverse=True) # 내림차순 정렬
    answer = ''
    for num in nums_order:
        answer += num * nums[num]
    return answer
