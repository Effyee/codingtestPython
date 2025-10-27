import sys
input=sys.stdin.readline

n=int(input())

def is_prime(n):
    isthisprime = [True] * (n + 1)
    isthisprime[0] = False
    isthisprime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if isthisprime[i]:
            for j in range(i * 2, n + 1, i):
                isthisprime[j] = False
    return [i for i in range(2,n+1) if isthisprime[i]]

arr=is_prime(n)
l=len(arr)
left,right,re=0,0,0
answer=0
while left<l and right<l:
    if re<n:
        re+=arr[right]
        right+=1
    if re>n:
        re-=arr[left]
        left+=1
    if re==n:
        answer+=1
        re -= arr[left]
        left += 1
print(answer)