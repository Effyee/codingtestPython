def solution(record):
    answer = []
    user_dict = {}

    # 각 사용자의 마지막 닉네임을 추적
    for r in record:
        details = r.split()
        action = details[0]
        user_id = details[1]

        if action in ['Enter', 'Change']:
            nickname = details[2]
            user_dict[user_id] = nickname

    # 메시지 생성
    for r in record:
        details = r.split()
        action = details[0]
        user_id = details[1]

        if action == 'Enter':
            answer.append(f"{user_dict[user_id]}님이 들어왔습니다.")
        elif action == 'Leave':
            answer.append(f"{user_dict[user_id]}님이 나갔습니다.")

    return answer