import sys
input=sys.stdin.readline

# 어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않는 경우
min_,max_=map(int,input().split())
check=[False]*(max_-min_+1)
i=2
while i*i<=max_:
    square=i*i
    start_index=(min_+square-1)//square*square

    for j in range(start_index,max_+1,square):
        if j>=min_:
            check[j-min_]=True
    i+=1
print(check.count(False))
