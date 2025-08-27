t = int(input())
res = []

for _ in range(t):
    n = int(input())
    phonebook = []
    for _ in range(n):
        phonebook.append(input())
    phonebook.sort() # 사전 순으로 정렬
    for i in range(n - 1):
        if phonebook[i] == phonebook[i + 1][:len(phonebook[i])]: #포합되는 수가 있는지 확인
            res.append('NO')
            break
    else: res.append('YES')

for result in res: # 결과 출력
    print(result)