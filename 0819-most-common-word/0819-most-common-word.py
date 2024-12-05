from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s=''
        for char in paragraph:
            if char.isalpha():
                s+=char.lower()
            else:
                s+=' '
        s=s.split()
        word_count=defaultdict(int)
        for word in s:
            if word not in banned:
                word_count[word]+=1
        
        return max(word_count,key=word_count.get)