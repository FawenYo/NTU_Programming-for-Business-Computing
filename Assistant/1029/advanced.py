def main():
    num_one = int(input())
    num_two = int(input())
    answer = calculate(num_one=num_one, num_two=num_two)
    print(answer)


def calculate(num_one, num_two):
    """
    # Faster version
    while num_two != 0:
        temp = num_two
        num_two = num_one % num_two
        num_one = temp
    return num_one
    """
    result = 1
    for each in range(1, min(num_one, num_two) + 1):
        if num_one % each == 0 and num_two % each == 0:
            result = each
    return result


if __name__ == "__main__":
    main()
