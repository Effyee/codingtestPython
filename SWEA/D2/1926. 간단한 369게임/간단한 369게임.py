n=input()

lst=[]
answer=0
for i in range(1,int(n)+1):
    if i<10:
        if i in [3,6,9]:
            print('-',end=' ')
        else:
            print(i,end=' ')
    else:
        lst=[]
        for n in str(i):
            lst.append(n)
        for l in lst:
            if '3'==l:
                answer+=1
            elif '6'==l:
                answer+=1
            elif '9'==l:
                answer+=1
        if answer==0:
            print(i,end=' ')
        else:
            print('-'*answer,end=' ')
            answer=0


        answer=0
        lst=[]