n=int(input())

def solution(n):
    if n==1:
        return 1
    start=2
    for i in range(n):
        if start<=n<start+6*i:
            return i+1
        start=start+6*i

print(solution(n))