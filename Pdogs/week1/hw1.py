def main():
    x1 = input()
    x2 = input()
    p1 = input()
    p2 = input()
    t = input()
    try:
        total_price, make_change = calculate(
            x1=int(x1), x2=int(x2), p1=int(p1), p2=int(p2), t=int(t)
        )
        print("{},{},{}".format(t, total_price, make_change))
    # Input data 可能非 int type
    except ValueError:
        print("Input Value Error!")


def calculate(x1, x2, p1, p2, t):
    # 全票價格
    full_ticket_price = x1 * p1
    # 學生票價格
    concession_ticket_price = x2 * p2
    # 應付金額
    total_price = full_ticket_price + concession_ticket_price
    # 找零金額
    make_change = t - total_price
    return total_price, make_change


if __name__ == "__main__":
    main()
