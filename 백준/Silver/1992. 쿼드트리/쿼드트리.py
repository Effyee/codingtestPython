import sys
input=sys.stdin.readline

# 흰점: 0, 검은 점:1
# 같은 숫자의 점들이 몰려있다면 압축할 수 있음
# 4개의 영역을 압축한 결과
n=int(input())
arr=[list(map(int,input().strip())) for _ in range(n)]
re=''

def merge_sort(row,col,length):
    global re
    s=arr[row][col]
    flag=True

    for i in range(row,row + length):
        for j in range(col, col + length):
            if s!=arr[i][j]:
                flag=False
        if not flag:
            break

    if flag:
        re+=str(s)
        return

    if length == 1:
        re += str(arr[row][col])
        return

    # 4분할
    re += '('
    half = length // 2
    merge_sort(row, col, half)  # 좌상단
    merge_sort(row, col + half, half)  # 우상단
    merge_sort(row + half, col, half)  # 좌하단
    merge_sort(row + half, col + half, half)  # 우하단
    re+=')'
    return

merge_sort(0,0,n)
print(re)