while True:
    numbers=list(map(int,input().split()))
    if numbers[0]==numbers[1]==numbers[2]==0:
        break
    else:
        numbers.sort()
        if numbers[0]+numbers[1]<=numbers[2]:
            print("Invalid")
            continue
        elif numbers[0]==numbers[1]==numbers[2]:
            print("Equilateral")
            continue
        elif (numbers[0]==numbers[1]) or (numbers[1]==numbers[2]):
            print("Isosceles")
            continue
        else:
            print("Scalene")