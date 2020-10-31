import math


def main():
    mode = int(input())
    number = int(input())
    answer = calculate(mode=mode, number=number)
    print(answer)


def calculate(mode, number):
    if mode == 1:
        result = math.log(number, 2)
    elif mode == 2:
        result = math.log(number, math.e)
    else:
        result = number ** 2
    return float(result)


if __name__ == "__main__":
    main()
