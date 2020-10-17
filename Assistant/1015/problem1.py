NUMBERS = 0
DOWN_LIMIT = 0
TOP_LIMIT = 0


def main():
    global NUMBERS, DOWN_LIMIT, TOP_LIMIT
    NUMBERS, DOWN_LIMIT, TOP_LIMIT = [int(i) for i in input().split(",")]
    input_nums = [int(i) for i in input().split(",")]
    answer = solution(input_nums=input_nums)
    print(answer)


def solution(input_nums):
    result = 0
    for each in input_nums:
        if DOWN_LIMIT <= each <= TOP_LIMIT:
            result += 1
    return result


if __name__ == "__main__":
    main()
