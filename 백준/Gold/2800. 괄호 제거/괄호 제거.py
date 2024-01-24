import sys
from itertools import combinations
s=sys.stdin.readline().rstrip()

loc=[]
stack=[]
for i in range(len(s)):
    if s[i]=='(':
        stack.append(i)
    elif s[i]==')':
        loc.append((stack.pop(),i))

answer=set()
for i in range(1, len(loc)+1):
    for c in combinations(loc, i):
        target = list(s)
        for k in c:
            target[k[0]] = ''
            target[k[1]] = ''
        answer.add(''.join(target))

answer = sorted(list(answer))
print('\n'.join(answer))
