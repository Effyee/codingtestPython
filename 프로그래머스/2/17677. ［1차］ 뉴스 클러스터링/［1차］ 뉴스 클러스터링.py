import re
from collections import Counter

def make_multiset(s):
    s = s.lower()
    multiset = []
    for i in range(len(s) - 1):
        if s[i:i+2].isalpha():
            multiset.append(s[i:i+2])
    return multiset

def solution(str1, str2):
    A = make_multiset(str1)
    B = make_multiset(str2)
    
    counterA = Counter(A)
    counterB = Counter(B)
    
    intersection = list((counterA & counterB).elements())
    union = list((counterA | counterB).elements())
    
    if len(union) == 0:
        return 65536
    
    jaccard_similarity = len(intersection) / len(union)
    
    return int(jaccard_similarity * 65536)
