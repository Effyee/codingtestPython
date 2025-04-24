import sys
from collections import Counter
input=sys.stdin.readline

word=str(input().rstrip())
word=word.upper()
C=Counter(word)
l=sorted(list(C.items()),key=lambda x:x[1],reverse=True)
if len(l)==1:
    print(l[0][0])
else:
    if l[0][1]==l[1][1]:
        print('?')
    else:
        print(l[0][0])