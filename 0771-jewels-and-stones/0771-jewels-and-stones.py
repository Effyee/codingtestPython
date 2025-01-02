class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer=0
        jewel=[]
        for s in jewels:
            jewel.append(s)
        
        for j in jewel:
            answer+=stones.count(j)
        return answer