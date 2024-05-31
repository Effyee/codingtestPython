def solution(brown, yellow):
    answer = []
    total=brown+yellow
    for r in range(3,total+1):
        c=total/r
        if (r-2)*(c-2)==yellow:
            return [c,r]