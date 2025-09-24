# 입력
expr = input().strip()

# '-' 기준으로 나누기
parts = expr.split('-')

# 첫 번째 부분은 그대로 합
total = sum(map(int, parts[0].split('+')))

# 나머지 부분은 전부 더한 뒤 빼기
for part in parts[1:]:
    total -= sum(map(int, part.split('+')))

# 결과 출력
print(total)
