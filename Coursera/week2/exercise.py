def main():
    input_list = []
    for index in range(4):
        user_input = input()
        input_list.append(int(user_input))
    print(calculate(input_list=input_list))


def calculate(input_list):
    amount = input_list[0] * 50 + input_list[1] * 10 + input_list[2] * 5 + input_list[3]
    return amount


if __name__ == "__main__":
    main()
