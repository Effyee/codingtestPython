import sys
from collections import defaultdict
input=sys.stdin.readline

n=int(input())
books=defaultdict(int)
for _ in range(n):
    book=str(input().rstrip())
    books[book]+=1

books=sorted(list(books.items()),key=lambda x:(-x[1],x[0]))
print(books[0][0])