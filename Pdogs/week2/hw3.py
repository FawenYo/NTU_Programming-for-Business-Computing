# Init variable
previous_interval_amount = 0
pay_amount = 0
done = False

# 級距個數
interval_amount = int(input())
# 最少需要購買的食材公斤數
demand = int(input())

for i in range(interval_amount):
    # 級距數量
    class_interval_amount = int(input())
    # 級距單價
    class_interval_price = int(input())

    # 達到目標級距
    if demand < class_interval_amount:
        # 尚未完成購買
        if not done:
            # 該級距應付金額 = (需求量 - 上一個級距的數量) * 級距單價
            pay_amount += (demand - previous_interval_amount) * class_interval_price
            done = True
    else:
        # 該級距應付金額 = (級距數量 - 上一個級距的數量) * 級距單價
        pay_amount += (
            class_interval_amount - previous_interval_amount
        ) * class_interval_price
        previous_interval_amount = class_interval_amount

print(pay_amount)
