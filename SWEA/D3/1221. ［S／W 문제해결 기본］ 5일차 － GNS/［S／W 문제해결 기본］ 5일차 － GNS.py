tc=int(input())

for _ in range(10):
    arr={"ZRO":0,"ONE":1,"TWO":2,"THR":3,"FOR":4,"FIV":5,"SIX":6,"SVN":7,"EGT":8,"NIN":9}

    tc,n=input().split()
    l=list(input().split())
    ll=[]

    for i in range(len(l)):
        ll.append([arr[l[i]],l[i]])

    ll.sort()
    answer=[]
    for i in range(len(l)):
        answer.append(ll[i][1])


    print(tc,' '.join(answer))