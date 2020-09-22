from Coursera.week2 import hw


def main():
    calculate_list = [500, 100, 50, 10, 5, 1]
    return_amounts = hw.calculate(input_num=input("input num:"))
    print(
        "; ".join(
            "{}, {}".format(calculate_list[index], value)
            for index, value in enumerate(return_amounts)
            if value != 0
        )
    )


if __name__ == "__main__":
    main()
