from itertools import permutations
def check(number):
    if number<=1:
        return False
    else:
        for i in range(2,int((number)**(1/2)+1)):
            if number%i==0:
                return False
        return True
def solution(numbers):
    answer = 0
    numbers=list(map(int,list(numbers)))
    num_list=[]
    for i in range(1,len(numbers)+1):
        for p in permutations(numbers,i):
            if int(''.join(map(str,p))) not in num_list:
                num_list.append(int(''.join(map(str,p))))
    for num in num_list:
        if check(num):
            answer+=1
    return answer