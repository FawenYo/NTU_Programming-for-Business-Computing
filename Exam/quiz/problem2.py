def main():
    # 便當價格, 飲料價格, 折價優惠
    data = [int(i) for i in input().split(",")]
    # 使用者行為
    customer_action = [int(i) for i in input().split(",")]

    launch_num, drink_num, revenue = solution(
        data=data, customer_action=customer_action
    )
    print(launch_num + "," + drink_num + "," + revenue)


def solution(data, customer_action):
    launch_num = 0
    drink_num = 0
    revenue = 0

    # 便當價格
    launch_price = data[0]
    # 飲料價格
    drink_price = data[1]
    # 折價優惠
    discount = data[2]

    for each in customer_action:
        # 只買便當
        if each == 1:
            launch_num += 1
            revenue += launch_price
        # 只買飲料
        elif each == 2:
            drink_num += 1
            revenue += drink_price
        # 買便當 ＆ 飲料
        else:
            launch_num += 1
            drink_num += 1
            result = launch_price + drink_price - discount
            if result < 0:
                result = 0
            revenue += result
    return str(launch_num), str(drink_num), str(revenue)


if __name__ == "__main__":
    main()
