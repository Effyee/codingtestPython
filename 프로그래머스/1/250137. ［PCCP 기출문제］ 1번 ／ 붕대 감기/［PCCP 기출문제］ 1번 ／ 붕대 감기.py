def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health

    attack_idx = 0
    success = 0

    last_time = attacks[-1][0]

    for time in range(1, last_time + 1):

        # 공격 받는 시간
        if time == attacks[attack_idx][0]:
            damage = attacks[attack_idx][1]

            health -= damage
            if health <= 0:
                return -1

            success = 0
            attack_idx += 1

        # 회복 시간
        else:
            success += 1

            health += x

            if success == t:
                health += y
                success = 0

            health = min(health, max_health)

    return health