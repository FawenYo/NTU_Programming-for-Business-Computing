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
    # 總支付金額, 原始支付金額, 最佳支付金額
    total_pay = origin_pay = best_pay = 0
    # 最佳支付數量
    best_amount = 0
    done = False

    for index in range(0, TOTAL_CLASS):
        # 級距數量
        class_interval_amount = user_inputs[index]
        # 級距單價
        class_interval_price = user_inputs[index + TOTAL_CLASS]

        # 該級距應付金額 = (級距數量 - 上一個級距的數量) * 級距單價
        interval_amount = (
            class_interval_amount - previous_interval_amount
        ) * class_interval_price

        total_pay += interval_amount

        if DEMAND <= class_interval_amount:
            # 尚未達到需求數量
            if not done:
                # 該級距應付金額 = (需求量 - 上一個級距的數量) * 級距單價
                origin_pay += (DEMAND - previous_interval_amount) * class_interval_price
                done = True

                if total_pay <= origin_pay:
                    best_pay = total_pay
                    best_amount = class_interval_amount
                else:
                    best_pay = origin_pay
                    best_amount = DEMAND

            else:
                if total_pay <= best_pay:
                    best_pay = total_pay
                    best_amount = class_interval_amount
        else:
            origin_pay += interval_amount
        previous_interval_amount = class_interval_amount

    return str(best_amount) + "," + str(best_pay)


if __name__ == "__main__":
    main()
