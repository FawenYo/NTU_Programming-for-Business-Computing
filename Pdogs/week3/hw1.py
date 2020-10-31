def main():
    # 補全成4位數
    data = "{:0<4d}".format(int(input()))
    results = []

    # 重複3次
    while not results or results[-1] != "6174":
        data = calculate(data="{:0<4d}".format(int(data)))
        results.append(data)
    print(",".join(each for each in results))


def calculate(data):
    input_numbers = sorted([int(i) for i in data])
    # 最小值
    num_one = input_numbers[0]
    num_two = input_numbers[1]
    num_three = input_numbers[2]
    # 最大值
    num_four = input_numbers[3]

    min_data = num_one * 1000 + num_two * 100 + num_three * 10 + num_four
    max_data = num_four * 1000 + num_three * 100 + num_two * 10 + num_one

    result = max_data - min_data
    return str(result)


if __name__ == "__main__":
    main()
