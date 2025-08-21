from itertools import permutations

def isprime(m):
    l = [False] * (m + 1)
    l[0] = l[1] = True
    for i in range(2, int(m**0.5) + 1):
        if not l[i]:
            for j in range(i*i, m+1, i):
                l[j] = True
    return l

def solution(numbers):
    answer = 0
    li = set()
    number = list(map(int, numbers.strip()))
    
    for i in range(1, len(number) + 1):
        li |= {int(''.join(map(str, p))) for p in permutations(number, i)}
    
    m = max(li)
    l = isprime(m)
    
    for x in li:
        if not l[x]:
            answer += 1
    return answer
