t = int(input())  # 테스트 케이스의 수를 입력받음

for i in range(t):
    numbers = list(map(int, input().split()))  # 공백으로 구분된 여러 숫자를 입력받아 정수 리스트로 변환
    answer = 0
    for number in numbers:
        if number % 2 == 1:  # 숫자가 홀수인 경우
            answer += number  # answer에 더함

    print('#' + str(i+1) + ' ' + str(answer))  # 결과 출력
