while True:
    try:
        a, b, c = map(int, input().split())
        if a == b == c == 0:
            break
        
        # 가장 긴 변을 c로 설정
        a, b, c = sorted([a, b, c])
        
        # 피타고라스 정리 검사
        if a*a + b*b == c*c:
            print("right")
        else:
            print("wrong")
    except EOFError:
        break
