ITEM_NUMS = 0
BOX_CAPABILITY = 0
ITEMS_WEIGHT = []


def main():
    global ITEM_NUMS, BOX_CAPABILITY, ITEMS_WEIGHT
    ITEM_NUMS, BOX_CAPABILITY = [int(i) for i in input().split(",")]
    ITEMS_WEIGHT = [int(i) for i in input().split(",")]
    # 排序 (大->小)
    ITEMS_WEIGHT.sort(reverse=True)
    answer = solution()
    print(answer)


def solution():
    boxes = [BOX_CAPABILITY for i in range(ITEM_NUMS)]
    for each in ITEMS_WEIGHT:
        for index, value in enumerate(boxes):
            if each <= value:
                value -= each
                boxes[index] = value
                break
    return len([x for x in boxes if x != BOX_CAPABILITY])


if __name__ == '__main__':
    main()
