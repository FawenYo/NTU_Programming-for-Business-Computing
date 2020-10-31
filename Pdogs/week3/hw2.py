TOTAL_CLASS = 0
DEMAND = 0


def main():
    global TOTAL_CLASS, DEMAND
    # 總級距數量, 最少需要購買的食材公斤數
    TOTAL_CLASS, DEMAND = [int(i) for i in input().split(",")]
    user_inputs = [int(i) for i in input().split(",")]
    print(calculate(user_inputs=user_inputs))


def calculate(user_inputs):
    # 上一個級距的數量
    previous_interval_amount = 0
    pay_amount = 0

    for index in range(0, int(len(user_inputs) / 2)):
        # 級距數量
        class_interval_amount = user_inputs[index]
        # 級距單價
        class_interval_price = user_inputs[index + TOTAL_CLASS]
        if DEMAND < class_interval_amount:
            # 該級距應付金額 = (需求量 - 上一個級距的數量) * 級距單價
            pay_amount += (DEMAND - previous_interval_amount) * class_interval_price
            return pay_amount
        else:
            # 該級距應付金額 = (級距數量 - 上一個級距的數量) * 級距單價
            pay_amount += (
                class_interval_amount - previous_interval_amount
            ) * class_interval_price
            previous_interval_amount = class_interval_amount
    return pay_amount


if __name__ == "__main__":
    main()
