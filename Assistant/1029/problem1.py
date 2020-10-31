def main():
    mode = int(input())
    number_one = float(input())
    number_two = float(input())
    answer = calculate(mode=mode, number_one=number_one, number_two=number_two)
    print(answer)


def calculate(mode, number_one, number_two):
    if mode == 1:
        result = number_one + number_two
    elif mode == 2:
        result = number_one - number_two
    else:
        result = number_one * number_two
    return float(result)


if __name__ == "__main__":
    main()
