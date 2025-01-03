from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n==1:
            return [[1]]
        nums=[i for i in range(1,n+1)]
        return list(combinations(nums,k))