class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # 왼쪽→오른쪽
        left_num = 1
        for i in range(n):
            answer[i] *= left_num
            left_num *= nums[i]
        
        # 오른쪽→왼쪽
        right_num = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right_num
            right_num *= nums[i]
        
        return answer
