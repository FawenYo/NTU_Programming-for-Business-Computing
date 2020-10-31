def main():
    number = int(input())
    answer = calculate(number=number)
    print(answer)


def calculate(number):
    result = 0
    # F(0) = 0
    first = 0
    # F(1) = 1
    second = 1
    for each in range(number - 1):
        result = first + second
        first = second
        second = result
    return result


if __name__ == "__main__":
    main()
