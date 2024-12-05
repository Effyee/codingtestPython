class Solution:
    def isPalindrome(self, s: str) -> bool:
        answer=''
        for char in s:
            if char.isalnum():
                answer+=char.lower()
        
        m=len(answer)//2
        return answer[:m]==answer[::-1][:m]