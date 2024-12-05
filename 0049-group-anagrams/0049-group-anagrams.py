from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=defaultdict(int)
        for s in strs:
            s=''.join(sorted(s))
            if s not in anagrams:
                anagrams[s]=len(anagrams)
        answer=[[] for _ in range(len(anagrams))]
        for s in strs:
            sorted_s=''.join(sorted(s))
            answer[anagrams[sorted_s]].append(s)
        return answer
        