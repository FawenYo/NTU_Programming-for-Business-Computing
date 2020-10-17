ITEM_NUM = 0
BACKPACK_CAPABILITY = 0


def main():
    global ITEM_NUM, BACKPACK_CAPABILITY
    ITEM_NUM, BACKPACK_CAPABILITY = [int(i) for i in input().split(",")]
    items_weight = [int(i) for i in input().split(",")]
    items_utility = [int(i) for i in input().split(",")]
    items_available = [int(i) for i in input().split(",")]
    answer = solution(
        items_weight=items_weight,
        items_utility=items_utility,
        items_available=items_available,
    )
    print(answer)


def solution(items_weight, items_utility, items_available):
    # 總負重
    space = 0
    # 總效用
    utility = 0

    for index, value in enumerate(items_available):
        # 有攜帶
        if value == 1:
            space += items_weight[index]
            utility += items_utility[index]
    if space <= BACKPACK_CAPABILITY:
        return "{},{}".format(space, utility)
    else:
        return "-1"


if __name__ == "__main__":
    main()
