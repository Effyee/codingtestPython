from itertools import combinations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums=[[],[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l']
        ,['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        if digits=="":
            return []
        li=[]
        for s in digits:
            li.append(nums[int(s)])
        answer= [''.join(combo) for combo in product(*li)]
        return answer