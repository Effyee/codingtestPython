import sys

words=list(sys.stdin.readline().strip())
alphabets=[0]*26

for i in range(len(words)):
    if words[i].islower():
        words[i]=words[i].upper()

for word in words:
    alphabets[ord(word)-65]+=1

m=max(alphabets)
count=0

index=0
for word in set(words):
    if alphabets[ord(word)-65]==m:
        index=ord(word)-65
        count+=1

if count>1:
    print('?')
else:
    print(chr(index+65))