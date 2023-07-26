def solution(nums):
    unique_poncketmon=len(set(nums))
    if unique_poncketmon<len(nums)//2:
        return unique_poncketmon
    else:
        return len(nums)//2