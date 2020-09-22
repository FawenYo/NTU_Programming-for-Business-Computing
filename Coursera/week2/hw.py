def calculate(input_num):
    amount = int(input_num)
    return_amount = return_total = 1000 - amount
    # return five hundred
    return_fh = return_total // 500
    return_amount = return_amount - return_fh * 500
    # return one hundred
    return_oh = return_amount // 100
    return_amount = return_amount - return_oh * 100
    # return fifty
    return_fifty = return_amount // 50
    return_amount = return_amount - return_fifty * 50
    # return ten
    return_ten = return_amount // 10
    return_amount = return_amount - return_ten * 10
    # return five
    return_five = return_amount // 5
    return_amount = return_amount - return_five * 5

    return return_fh, return_oh, return_fifty, return_ten, return_five, return_amount


if __name__ == "__main__":
    five_hundred, one_hundred, fifty, ten, five, one = calculate(input_num=input("input num:"))
    print(f"{five_hundred} {one_hundred} {fifty} {ten} {five} {one}")
