def main():
    input_list = []
    # 輸入順序: 全票數量, 全票價格, 學生票數量, 學生票價格, 總支付金額, 購票上限
    for index in range(6):
        user_input = input()
        input_list.append(int(user_input))
    raw_ticket_left, raw_return_amount = calculate(input_list=input_list)
    # "尚可購買張數" < 0 則輸出 "-1"
    if raw_ticket_left >= 0:
        ticket_left = str(raw_ticket_left)
    else:
        ticket_left = "-1"
    # "找錢金額"" < 0 則輸出 "-2"
    if raw_return_amount >= 0:
        return_amount = "$" + str(raw_return_amount)
    else:
        return_amount = "-2"
    print(ticket_left + "," + return_amount)


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
    # 購票上限
    ticket_limit = input_list[5]

    # 尚可購買張數 = 購票上限 - 全票數量 - 學生票數量
    ticket_left = ticket_limit - full_ticket_quantity - concession_ticket_quantity

    # 全票金額 = 全價數量 * 全票價格
    full_ticket_amount = full_ticket_quantity * full_ticket_price
    # 學生票金額 = 學生價數量 * 學生票價格
    concession_ticket_amount = concession_ticket_quantity * concession_ticket_price
    # 找錢金額 = 總支付金額 - 全票金額 - 學生票金額
    return_amount = total_amount - full_ticket_amount - concession_ticket_amount
    return ticket_left, return_amount


if __name__ == "__main__":
    main()
