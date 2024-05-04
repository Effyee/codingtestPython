t=int(input())

for _ in range(t):
    max_value=0
    n=int(input())
    numbers=[0]*(101)

    score_list=list(map(int,input().split()))

    for score in score_list:
        numbers[score]+=1

    answer=[]
    for i in range(len(numbers)):
        if numbers[i]>max_value:
            max_value=numbers[i]
            answer=[]
            answer.append(i)
        elif numbers[i]==max_value:
            answer=[]
            answer.append(i)

    print('#'+str(_+1), ' '.join(map(str, answer)))