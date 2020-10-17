def main():
    # 便當價格
    launch_price = int(input())
    # 飲料價格
    drink_price = int(input())
    # 折價優惠
    discount = int(input())

    answer = solution(
        launch_price=launch_price, drink_price=drink_price, discount=discount
    )
    print(answer)


def solution(launch_price, drink_price, discount):
    result = launch_price + drink_price - discount
    if result >= 0:
        return result
    else:
        return 0


if __name__ == "__main__":
    main()
