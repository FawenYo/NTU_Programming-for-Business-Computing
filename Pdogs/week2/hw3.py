# 全票數量
full_ticket_quantity = int(input())
# 全票價格
full_ticket_price = int(input())
# 學生票數量
concession_ticket_quantity = int(input())
# 學生票價格
concession_ticket_price = int(input())
# 總支付金額
total_amount = int(input())
# 購票上限
ticket_limit = int(input())

# 尚可購買張數 = 購票上限 - 全票數量 - 學生票數量
ticket_left = ticket_limit - full_ticket_quantity - concession_ticket_quantity

# 全票金額 = 全價數量 * 全票價格
full_ticket_amount = full_ticket_quantity * full_ticket_price
# 學生票金額 = 學生價數量 * 學生票價格
concession_ticket_amount = concession_ticket_quantity * concession_ticket_price
# 找錢金額 = 總支付金額 - 全票金額 - 學生票金額
return_amount = total_amount - full_ticket_amount - concession_ticket_amount

# "找錢金額" < 0 則不顯示
if return_amount >= 0:
    output_return_amount = "$" + str(return_amount)
else:
    output_return_amount = ""

# "尚可購買張數" < 0 則不顯示
if ticket_left >= 0:
    output_ticket_left = str(ticket_left)
    print(output_ticket_left, output_return_amount, sep=",")
else:
    print(output_return_amount)
