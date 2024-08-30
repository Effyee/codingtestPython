from collections import Counter

def solution(k, tangerine):
    answer = 0
    box = Counter(tangerine)  # 귤 종류별 수를 세기 위해 Counter 사용
    counts = sorted(box.values(), reverse=True)  # 귤의 수를 내림차순으로 정렬

    for count in counts:
        answer += 1  # 종류 수 증가
        k -= count  # 현재 종류의 귤 개수만큼 빼기
        if k <= 0:  # k가 0 이하가 되면 종료
            break

    return answer

# 테스트
print(solution(k=6, tangerine=[1, 3, 2, 5, 4, 5, 2, 3]))
