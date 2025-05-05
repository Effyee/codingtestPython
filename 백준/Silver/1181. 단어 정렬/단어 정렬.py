import sys
input=sys.stdin.readline

n=int(input())
words=sorted(list(set(str(input().strip()) for _ in range(n))),key=lambda x:(len(x),x))
for word in words:
    print(word)