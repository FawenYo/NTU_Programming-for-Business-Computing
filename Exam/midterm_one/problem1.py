FIRST_NUMBER = 0
SECOND_NUMBER = 0


def main():
    global FIRST_NUMBER, SECOND_NUMBER
    FIRST_NUMBER = int(input())
    SECOND_NUMBER = int(input())
    answer = solution()
    print(answer)


def solution():
    result = FIRST_NUMBER - SECOND_NUMBER
    if result >= 0:
        return result
    else:
        return 0


if __name__ == "__main__":
    main()
