def calculate(input_num):
    amount = int(input_num)
    return_amount = return_total = 1000 - amount

    calculate_list = [500, 100, 50, 10, 5, 1]
    return_amount_list = []
    for value in calculate_list:
        return_value = return_amount // value
        return_amount_list.append(return_value)
        return_amount -= return_value * value
    return return_amount_list


if __name__ == "__main__":
    print(", ".join(str(i) for i in calculate(input_num=input("input num:"))))
