from math import prod
def solution(brown, yellow):
    answer = []
    total=brown+yellow
    yellowlist=[]
    
    for i in range(1,total+1):
        if yellow%i==0:
            yellowlist.append([i+2,(yellow//i)+2])
    
    for yellows in yellowlist:
        if prod(yellows)==total:
            return sorted(yellows,reverse=True)
            
            
  