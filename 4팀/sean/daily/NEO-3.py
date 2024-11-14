def solution(powers, monsters):
    result = []
    n = len(monsters)
    for power in powers:
        can = can_kill_all_monsters(power, monsters)
        result.append(can)
    return result

def can_kill_all_monsters(power, monsters):
    t_i_max_list = [] # 사냥 가능한 마지막 시간
    for monster in monsters:
        initial_power, per_second_increase = monster
        numerator = power - 1 - initial_power
        if numerator < 0:
            # 몬스터를 사냥 x
            return 0
        t_i_max = numerator // per_second_increase
        if t_i_max < 0:
            # 몬스터를 사냥 x
            return 0
        t_i_max_list.append(t_i_max)

    list.sort()
    for t in range(len(t_i_max_list)):
        if t > t_i_max_list[t]:
            # 시간 내에 몬스터를 사냥 x
            return 0
    return 1

# 테스트 케이스
if __name__ == "__main__":
    # 입출력 예 #1
    powers = [6, 5]
    monsters = [
        [2, 3],
        [1, 7],
        [1, 2]
    ]
    print(solution(powers, monsters))  # [1, 0]

    # 입출력 예 #2
    powers = [5, 6, 7]
    monsters = [
        [2, 2],
        [3, 1],
        [1, 1],
        [6, 2]
    ]
    print(solution(powers, monsters))  # [0, 0, 1]

    # 추가 테스트 케이스
    powers = [10, 15, 20]
    monsters = [
        [1, 1],
        [1, 1],
        [2, 2],
        [10, 1]
    ]
    print(solution(powers, monsters))  # [0, 1, 1]



