def main():
    # 補全成3位數
    data = "{:0<3d}".format(int(input()))
    results = []

    # 重複3次
    for i in range(3):
        data = calculate(data="{:0<3d}".format(int(data)))
        results.append(data)
    print(",".join(each for each in results))


def calculate(data):
    input_numbers = sorted([int(i) for i in data])
    # 最大值
    min_num = input_numbers[0]
    # 中間值
    medium_num = input_numbers[1]
    # 最小值
    max_num = input_numbers[2]

    max_data = max_num * 100 + medium_num * 10 + min_num
    min_data = min_num * 100 + medium_num * 10 + max_num
    result = max_data - min_data
    return str(result)


if __name__ == "__main__":
    main()
