for tc in range(1,11):
    n, number_string = input().split()
    n = int(n)
    arr = list(map(int, number_string))

    while True:
        found = False

        i = 0
        while i < len(arr) - 1:
            if arr[i] == arr[i + 1]:
                del arr[i:i + 2]
                found = True
            else:
                i += 1

        if not found:
            break

    print('#'+str(tc)+' '+''.join(map(str,arr)))
