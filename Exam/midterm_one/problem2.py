NUMBER_LIST = []


def main():
    global NUMBER_LIST
    total_numbers = int(input())
    NUMBER_LIST = [int(i) for i in input().split(",")]
    answer = solution()
    print(answer)


def solution():
    result_list = []
    for index, value in enumerate(NUMBER_LIST[:-1]):
        result = value - NUMBER_LIST[index + 1]
        if result < 0:
            result = 0
        result_list.append(result)
    return min(result_list)


if __name__ == "__main__":
    main()
