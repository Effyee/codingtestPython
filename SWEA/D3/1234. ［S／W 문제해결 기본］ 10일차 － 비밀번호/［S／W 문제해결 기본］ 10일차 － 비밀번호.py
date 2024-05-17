for _ in range(10):
    k=list(input().split())
    n=int(k[0])
    arr=list(map(int,k[1].strip()))
    i=0
    while True:
        while i<len(arr)-1:
            flag = True
            if arr[i]==arr[i+1]:
                del arr[i:i+2]
                i=0
                break
            else:
                flag=False
            i+=1
        else:
            i=0
        if flag==False:
            break

    print('#'+str(_+1)+' '+''.join(map(str,arr)))