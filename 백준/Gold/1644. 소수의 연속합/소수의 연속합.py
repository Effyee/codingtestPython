import sys
input = sys.stdin.readline

n = int(input())
primes = []

def findprime(n):
    global primes
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = [i for i, val in enumerate(is_prime) if val]

findprime(n)

start, end = 0, 0
total = 0
count = 0

while end <= len(primes):
    if total < n:
        if end < len(primes):
            total += primes[end]
        end += 1
    elif total > n:
        if start < len(primes):
            total -= primes[start]
        start += 1
    else:
        count += 1
        if end < len(primes):
            total += primes[end]
        end += 1

print(count)
