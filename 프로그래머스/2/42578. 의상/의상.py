from collections import defaultdict
from math import prod

def solution(clothes):
    counter = defaultdict(int)
    for _, type_ in clothes:
        counter[type_] += 1

    return prod([count + 1 for count in counter.values()]) - 1
