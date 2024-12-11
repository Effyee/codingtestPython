class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        answer = set()

        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if  sum == 0:
                    answer.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif sum < 0:
                    left+=1
                else:
                    right-=1
                
        answer = list(answer)
        return answer