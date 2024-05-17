from collections import deque

for _ in range(10):
    tc=int(input())
    arr=list(map(int,input().split()))
    password=deque(arr)

    i=1
    cnt=0
    while password[-1]!=0:
       if i<6:
           result = password.popleft()-i
           if result>0:
               password.append(result)
           else:
               password.append(0)
       else:
           i=0
       i+=1
       cnt+=1

    print('#'+str(_+1)+' '+' '.join(map(str,password)))