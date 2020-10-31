ITEM_NUM = 0
BACKPACK_CAPABILITY = 0


def main():
    global ITEM_NUM, BACKPACK_CAPABILITY

    ITEM_NUM, BACKPACK_CAPABILITY = [int(i) for i in input().split(",")]
    items_weight = [int(i) for i in input().split(",")]
    items_utility = [int(i) for i in input().split(",")]
    answer = solution(items_weight=items_weight, items_utility=items_utility)
    print(answer)


def solution(items_weight, items_utility):
    utility_one, list_one = algorithm_one(
        items_weight=items_weight, items_utility=items_utility
    )
    utility_two, list_two = algorithm_two(
        items_weight=items_weight, items_utility=items_utility
    )
    if utility_one >= utility_two:
        return ",".join(str(i) for i in sorted(list_one))
    else:
        return ",".join(str(i) for i in sorted(list_two))


# 演算法 - 1
def algorithm_one(items_weight, items_utility):
    space = 0
    utility = 0
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
            utility += __utility__
            answer_list.append(__index__)
    return utility, sorted(answer_list)


# 演算法 - 2
def algorithm_two(items_weight, items_utility):
    space = 0
    utility = 0
    answer_list = []

    # (編號, 重量, 效用)
    temp_list = [
        (index + 1, items_weight[index], items_utility[index])
        for index in range(ITEM_NUM)
    ]
    # 效用較大 > 重量較輕 > 編號較小
    sorted_list = sorted(temp_list, key=lambda tup: (-tup[2], tup[1], tup[0], tup[2]))
    for each in sorted_list:
        __index__ = each[0]
        __weight__ = each[1]
        __utility__ = each[2]
        temp_space = space + __weight__
        if temp_space <= BACKPACK_CAPABILITY:
            space = temp_space
            utility += __utility__
            answer_list.append(__index__)
    return utility, sorted(answer_list)


if __name__ == "__main__":
    main()
