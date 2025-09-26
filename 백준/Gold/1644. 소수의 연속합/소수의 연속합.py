import sys
input=sys.stdin.readline

# 연속된 소수의 합
n=int(input())

def find_prime(n):
    primes=[True]*(n+1)
    primes[0]=False
    primes[1]=False
    for i in range(2,int(n**(1/2))+1):
        if primes[i]:
            for j in range(i*2,n+1,i):
                primes[j]=False
    return [i for i in range(2,n+1) if primes[i]==True]

primes=find_prime(n)

left,right,total=0,0,0
answer=0
while right<len(primes):
    if total<n:
        total+=primes[right]
        right+=1
    if total>n:
        if left<right:
            total-=primes[left]
            left+=1
    if total==n:
        answer+=1
        if left<right:
            total-=primes[left]
            left+=1
print(answer)
