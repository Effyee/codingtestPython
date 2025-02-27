import sys
input=sys.stdin.readline

def cal(a,op,b):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    else:
        return a*b

answer=-int(1e9)

def backtrack(index,result):
    global answer
    if index>=len(ops):
        answer=max(answer,result)
        return
    #1. 현재 연산자에 괄호
    backtrack(index+1,cal(result,ops[index],nums[index+1]))
    #2. 다음 연산자에 괄호
    if index+1<len(ops):
        next_value=cal(nums[index+1],ops[index+1],nums[index+2])
        backtrack(index+2, cal(result,ops[index],next_value))

N=int(input())
s=input().strip()
nums,ops=[],[]

for i in range(N):
    if i%2==0:
        nums.append(int(s[i]))
    else:
        ops.append(s[i])

backtrack(0,nums[0])

print(answer)