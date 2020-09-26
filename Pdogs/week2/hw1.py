def main():
    input_list = []
    # 輸入順序: 全票數量, 全票價格, 學生票數量, 學生票價格, 總支付金額
    for index in range(5):
        user_input = input()
        input_list.append(int(user_input))
    return_amount = calculate(input_list=input_list)

    if return_amount >= 0:
        print("$" + str(return_amount))
    else:
        print("-1")


def calculate(input_list):
    # 全票數量
    full_ticket_quantity = input_list[0]
    # 全票價格
    full_ticket_price = input_list[1]
    # 學生票數量
    concession_ticket_quantity = input_list[2]
    # 學生票價格
    concession_ticket_price = input_list[3]
    # 總支付金額
    total_amount = input_list[4]

    # 全票金額 = 全價數量 * 全票價格
    full_ticket_amount = full_ticket_quantity * full_ticket_price
    # 學生票金額 = 學生價數量 * 學生票價格
    concession_ticket_amount = concession_ticket_quantity * concession_ticket_price
    # 找錢金額 = 總支付金額 - 全票金額 - 學生票金額
    return_amount = total_amount - full_ticket_amount - concession_ticket_amount
    return return_amount


if __name__ == "__main__":
    main()
