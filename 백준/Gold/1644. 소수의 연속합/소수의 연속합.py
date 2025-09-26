import sys
input=sys.stdin.readline

n=int(input())
def find_prime(n):
    isthisprime=[True]*(n+1)
    isthisprime[0]=False
    isthisprime[1]=False
    for i in range(2,int(n**0.5)+1):
        if isthisprime[i]:
            for j in range(i*2,n+1,i):
                isthisprime[j]=False
    return [i for i in range(1,n+1) if isthisprime[i]]

primes=find_prime(n)
left,right,result,answer=0,0,0,0
while right<len(primes):
    if result<n:
        result+=primes[right]
        right+=1
    if result>n:
        if left<right:
            result -= primes[left]
            left+=1
    if result==n:
        answer+=1
        if left < right:
            result -= primes[left]
            left += 1
    
print(answer)