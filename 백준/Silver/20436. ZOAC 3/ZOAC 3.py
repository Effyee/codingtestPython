import sys
input=sys.stdin.readline

keyboard=[['q','w','e','r','t','y','u','i','o','p'],
          ['a','s','d','f','g','h','j','k','l',''],
          ['z','x','c','v','b','n','m','','','']]

left_keys=set('qwertasdfgzxcv')
right_keys=set('yuiophjklbnm')

L,R=input().split()
letters=input().strip()

key_pos={}
for i in range(3):
    for j in range(10):
        if keyboard[i][j]:
            key_pos[keyboard[i][j]]=(i,j)

Lx,Ly=key_pos[L]
Rx,Ry=key_pos[R]

answer=0

for letter in letters:
    lx,ly=key_pos[letter]

    if letter in left_keys:  # 왼손으로 입력해야 하는 경우
        answer += abs(Lx - lx) + abs(Ly - ly) + 1
        Lx, Ly = lx, ly  # 왼손 위치 업데이트
    else:  # 오른손으로 입력해야 하는 경우
        answer += abs(Rx - lx) + abs(Ry - ly) + 1
        Rx, Ry = lx, ly  # 오른손 위치 업데이트

print(answer)