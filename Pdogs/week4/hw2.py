ITEM_NUM = 0
BACKPACK_CAPABILITY = 0


def main():
    global ITEM_NUM, BACKPACK_CAPABILITY

    ITEM_NUM, BACKPACK_CAPABILITY = [int(i) for i in input().split(",")]
    items_weight = [int(i) for i in input().split(",")]
    items_utility = [int(i) for i in input().split(",")]
    answer = solution(items_weight=items_weight, items_utility=items_utility)
    print(answer)


def calculate_cp(items_weight, items_utility):
    cp_list = []
    for index, value in enumerate(items_utility):
        cp_value = value / items_weight[index]
        cp_list.append(cp_value)
    return cp_list


def solution(items_weight, items_utility):
    space = 0
    answer_list = []

    # (編號, 重量, 效用, CP值)
    temp_list = [
        (
            index + 1,
            items_weight[index],
            items_utility[index],
            items_utility[index] / items_weight[index],
        )
        for index in range(ITEM_NUM)
    ]
    # CP值較大 > 重量較輕 > 編號較小
    sorted_list = sorted(temp_list, key=lambda tup: (-tup[3], tup[1], tup[0], tup[2]))
    for each in sorted_list:
        __index__ = each[0]
        __weight__ = each[1]
        __utility__ = each[2]
        temp_space = space + __weight__
        if temp_space <= BACKPACK_CAPABILITY:
            space = temp_space
            answer_list.append(__index__)
    return ",".join(str(i) for i in sorted(answer_list))


if __name__ == "__main__":
    main()
